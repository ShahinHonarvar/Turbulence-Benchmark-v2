def is_prime(n):
    if n in (0, 1):
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[175]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            trunc = num
            while trunc > 1:
                trunc //= 10
                if not is_prime(trunc):
                    break
            else:
                primes.append(num)
    return sorted(primes)