def sum_of_divisors_in_range(n):

    def divisors(k):
        return [d for d in range(1, k + 1) if k % d == 0]
    divs = divisors(n)
    divs_in_range = [d for d in divs if 18 <= d <= 52]
    return sum(divs_in_range) if divs_in_range else 0