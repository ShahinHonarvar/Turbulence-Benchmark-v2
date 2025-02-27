def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(num_tuple: tuple) -> list:
    x = num_tuple[29]
    primes = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            trunc = num
            while trunc > 0:
                trunc = int(trunc / 10)
                if is_prime(trunc):
                    primes.append(num)
                    break
    return sorted(primes, reverse=True)