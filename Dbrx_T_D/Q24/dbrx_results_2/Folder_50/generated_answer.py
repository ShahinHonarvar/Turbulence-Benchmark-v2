def sum_of_divisors_in_range(n):

    def divisors(m):
        divs = set()
        for i in range(1, int(m ** 0.5) + 1):
            if m % i:
                continue
            divs.add(i)
            divs.add(m // i)
        return divs
    divs = divisors(n)
    divs_in_range = sum((div for div in divs if 57 <= div <= 86))
    return divs_in_range