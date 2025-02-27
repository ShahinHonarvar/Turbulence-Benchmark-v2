def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[8]
    prime_list = []

    def is_left_truncatable(n):
        m = n
        while m != 0:
            if m % 10 == 0 or not is_prime(m):
                return False
            m //= 10
        return True
    for i in range(2, x):
        if is_left_truncatable(i):
            prime_list.append(i)
    return sorted(prime_list, reverse=True)