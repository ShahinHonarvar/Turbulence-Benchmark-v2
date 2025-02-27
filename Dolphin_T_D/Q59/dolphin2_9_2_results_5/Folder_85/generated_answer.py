def all_left_truncatable_prime(lst):

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2):
            return False
        return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))
    x = lst[94]
    res = []
    for i in range(2, x):
        if is_prime(i):
            j = i
            while j != 0 and is_prime(j):
                j //= 10
            if j == 0:
                res.append(i)
    return sorted(res)