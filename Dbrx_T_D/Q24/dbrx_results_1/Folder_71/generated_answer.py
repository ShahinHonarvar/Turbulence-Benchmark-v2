def sum_of_divisors_in_range(n):

    def divisors(k):
        d = {1, k}
        for i in range(2, int(k ** 0.5) + 1):
            if k % i:
                continue
            d.add(i)
            d.add(k // i)
        return d
    d = divisors(n)
    d = {div for div in d if 45 <= div <= 72}
    return sum(d) if d else 0