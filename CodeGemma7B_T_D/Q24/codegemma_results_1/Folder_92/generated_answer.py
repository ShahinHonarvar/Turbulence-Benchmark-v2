def sum_of_divisors_in_range(num):
    if num % 2 == 0:
        sum = 0
        for divisor in range(8, 9 + 1):
            if num % divisor == 0:
                sum += divisor
        return sum