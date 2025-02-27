def is_prime(n):
    if n in (0, 1):
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[3]
    primes = []
    for num in range(x, 1, -1):
        if is_prime(num):
            trunc = num
            while trunc != 0 and is_prime(trunc):
                trunc //= 10
                if trunc > 1 and (not is_prime(trunc)):
                    break
                if trunc < 2:
                    primes.append(num)
    return sorted(primes, reverse=True)