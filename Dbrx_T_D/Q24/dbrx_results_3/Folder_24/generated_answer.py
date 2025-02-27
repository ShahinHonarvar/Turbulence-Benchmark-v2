def sum_of_divisors_in_range(n):

    def divisors(k):
        return [d for d in range(1, k + 1) if k % d == 0]

    def sum_of_divs(k):
        return sum(divisors(k))
    divisors_in_range = [i for i in divisors(n) if 43 <= i <= 95]
    return sum(divisors_in_range) if divisors_in_range else 0