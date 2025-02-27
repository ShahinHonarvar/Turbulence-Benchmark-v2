def all_right_truncatable_prime(int_tuple):
    x = int_tuple[91]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            trunc = num
            while trunc > 0:
                if not is_prime(trunc):
                    break
                trunc //= 10
            else:
                primes.append(num)
    return sorted(primes)

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(n ** 0.5) + 1
    for div in range(3, sqrt_n, 2):
        if n % div == 0:
            return False
    return True