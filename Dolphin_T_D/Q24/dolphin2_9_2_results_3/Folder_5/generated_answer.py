def sum_of_divisors_in_range(num):
    sum = 0
    for i in range(1, num + 1):
        if i >= 7 and i <= 8 and (num % i == 0):
            sum += i
    if sum > 0:
        return sum
    else:
        return 0