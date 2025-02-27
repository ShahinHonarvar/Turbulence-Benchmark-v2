def all_left_truncatable_prime(t):
    x = t[618]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    prime = []
    for n in range(2, x):
        if '0' in str(n):
            continue
        trunc = n
        while trunc:
            if not is_prime(trunc):
                break
            trunc //= 10
        else:
            prime.append(n)
    return sorted(prime)