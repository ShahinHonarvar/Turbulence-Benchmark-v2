def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[29]
    primes = []
    for i in range(2, x + 1):
        if is_prime(i) and ('0' not in str(i) and int(str(i)[1:-1]) > 0):
            while i > 9:
                if not is_prime(int(str(i)[1:-1])):
                    break
                i = int(str(i)[1:-1])
            else:
                primes.append(i)
    return sorted(primes)