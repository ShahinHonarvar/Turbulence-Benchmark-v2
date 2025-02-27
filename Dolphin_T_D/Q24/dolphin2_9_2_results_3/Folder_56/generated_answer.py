def sum_of_divisors_in_range(num):
    if num < 6 or num > 9:
        return 0
    else:
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        return sum(divisors)