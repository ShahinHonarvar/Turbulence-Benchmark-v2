def sum_of_divisors_in_range(n):

    def divisors(k):
        return [i for i in range(1, k + 1) if k % i == 0]
    divs = divisors(n)
    return sum([d for d in divs if 469 <= d <= 682])