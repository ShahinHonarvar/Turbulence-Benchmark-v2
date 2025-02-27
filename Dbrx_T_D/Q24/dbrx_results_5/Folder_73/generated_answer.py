def sum_of_divisors_in_range(n):

    def divisors(k):
        return [i for i in range(1, k + 1) if k % i == 0]
    divisors_of_n = divisors(n)
    divisors_in_range = [i for i in divisors_of_n if 46 <= i <= 89]
    if divisors_in_range:
        return sum(divisors_in_range)
    else:
        return 0