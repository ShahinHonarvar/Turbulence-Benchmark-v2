def sum_of_divisors_in_range(num):
    sum_divisors = 0
    for i in range(1, num + 1):
        if num % i == 0 and 70 <= i <= 72:
            sum_divisors += i
    return sum_divisors