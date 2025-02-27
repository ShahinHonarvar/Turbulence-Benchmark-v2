def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(num_tuple):
    num = num_tuple[429]
    primes = []
    for i in range(num - 1, 1, -1):
        if is_prime(i):
            trunc = i
            while trunc:
                if is_prime(trunc):
                    trunc //= 10
                else:
                    break
            else:
                primes.append(i)
    return primes