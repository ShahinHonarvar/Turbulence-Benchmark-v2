def all_left_truncatable_prime(index_tuple):
    x = index_tuple[39]
    left_truncatable_primes = [2]
    for i in range(3, x):
        if is_prime(i):
            truncated = i
            while truncated != 0:
                if not is_prime(truncated):
                    break
                truncated //= 10
            else:
                left_truncatable_primes.append(i)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes

def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True