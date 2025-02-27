def sum_of_divisors_in_range(n):

    def divisors_in_range(num, lower, upper):
        if num % lower == 0:
            return lower
        elif lower > upper:
            return 0
        else:
            return divisors_in_range(num, lower + 1, upper)
    sum_of_divisors = 0
    lower, upper = (615, 792)
    for divisor in range(lower, upper + 1):
        if n % divisor == 0:
            sum_of_divisors += divisors_in_range(divisor, 1, divisor)
    return sum_of_divisors if sum_of_divisors > 0 else 0