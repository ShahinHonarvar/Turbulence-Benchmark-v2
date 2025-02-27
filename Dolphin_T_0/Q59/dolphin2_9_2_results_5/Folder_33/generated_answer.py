def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tpl):

    def is_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        m = n
        while m > 0:
            if not is_prime(m):
                return False
            m = m // 10
        return True
    x = tpl[945]
    primes = [i for i in range(x - 1, 1, -1) if is_truncatable_prime(i)]
    return primes