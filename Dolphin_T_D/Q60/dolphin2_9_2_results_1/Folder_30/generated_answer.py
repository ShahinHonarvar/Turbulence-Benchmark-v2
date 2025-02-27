def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    primes = []
    for num in range(x, 1, -1):
        if '0' in str(num):
            continue
        while num > 1:
            if not is_prime(num):
                break
            num = int(str(num)[1:-1])
            if num < 2:
                continue
            primes.append(num)
    return sorted(primes, reverse=True)