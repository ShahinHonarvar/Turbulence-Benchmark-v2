def sum_of_divisors_in_range(n):

    def divisors(k):
        d = set()
        for i in range(1, int(k ** 0.5) + 1):
            if k % i:
                continue
            d.add(i)
            d.add(k // i)
        return d
    d = divisors(n)
    return sum((div for div in d if 392 <= div <= 465)) if d else 0