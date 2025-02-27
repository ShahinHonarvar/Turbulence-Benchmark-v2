def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[35]
    primes = []
    for num in range(x, 1, -1):
        if '0' in str(num) or not is_prime(num):
            continue
        while len(str(num)) > 2:
            if not is_prime(int(str(num)[1:-1])):
                break
            num = int(str(num)[1:-1])
        else:
            primes.append(num)
    return sorted(primes, reverse=True)