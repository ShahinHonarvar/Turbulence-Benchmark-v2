def sum_of_divisors_in_range(n):

    def is_divisible(x):
        return n % x == 0
    divisors = [i for i in range(14, 94) if is_divisible(i)]
    return sum(divisors) if divisors else 0