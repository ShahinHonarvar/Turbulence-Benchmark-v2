def sum_of_divisors_in_range(num):
    if num <= 0:
        return 0
    sum = 0
    for i in range(8, int(num ** 0.5) + 1):
        if num % i == 0 and (i >= 8 and i <= 9 or (num // i >= 8 and num // i <= 9)):
            sum += i + num // i
    return sum