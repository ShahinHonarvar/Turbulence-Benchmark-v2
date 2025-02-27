def sum_of_divisors_in_range(n):

    def divisors(k):
        return {t for t in range(1, k + 1) if k % t == 0}
    divs = divisors(n)
    divs_in_range = {d for d in divs if 59 <= d <= 88}
    return sum(divs_in_range) if divs_in_range else 0