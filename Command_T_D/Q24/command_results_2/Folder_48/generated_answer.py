def sum_of_divisors_in_range(n):
    for i in range(461, 827 + 1):
        if n % i == 0:
            if i * i == n:
                yield i
            elif i == 1 or i == n - 1:
                yield n
            else:
                for j in range(2, int(n ** 0.5) + 1):
                    if n % j == 0:
                        yield j
                        if n / j == j:
                            yield (n / j)
                        else:
                            yield (n / j)
                            for k in range(2, int(n / j ** 0.5) + 1):
                                if n / (j * k) == k:
                                    yield (n / (j * k))
                                else:
                                    yield (n / (j * k))