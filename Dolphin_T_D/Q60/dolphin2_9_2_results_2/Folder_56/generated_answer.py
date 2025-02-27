def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[30]
    primes = []
    for i in range(2, x + 1):
        if is_prime(i) and '0' not in str(i):
            left_right = i
            while len(str(left_right)) > 1:
                left_right = int(str(left_right)[1:-1])
                if not is_prime(left_right):
                    break
            else:
                primes.append(i)
    return sorted(primes)