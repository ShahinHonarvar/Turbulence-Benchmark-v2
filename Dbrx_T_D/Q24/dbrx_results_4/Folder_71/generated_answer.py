def sum_of_divisors_in_range(n):

    def divisors(k):
        return [d for d in range(1, k + 1) if k % d == 0]
    divs_in_range = sum((div for div in divisors(n) if 45 <= div <= 72))
    return divs_in_range if divs_in_range else 0