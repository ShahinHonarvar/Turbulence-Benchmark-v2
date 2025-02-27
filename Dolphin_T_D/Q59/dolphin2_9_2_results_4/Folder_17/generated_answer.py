def all_left_truncatable_prime(t):

    def truncatable_prime(n):
        return all((int(str(n)[i:]) % i == 0 for i in range(1, len(str(n))))) and all((int(str(n)[:i]) % i == 0 for i in range(1, len(str(n)))))
    x = list(t)[36]
    l = []
    for i in range(2, x):
        if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))):
            if truncatable_prime(i):
                l.append(i)
    return sorted(l, reverse=True)