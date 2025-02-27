def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    primes = []
    for num in range(2, x + 1):
        if is_prime(num):
            while len(str(num)) > 2:
                num = int(str(num)[1:-1])
                if not is_prime(num):
                    break
            else:
                primes.append(num)
    return sorted(primes)