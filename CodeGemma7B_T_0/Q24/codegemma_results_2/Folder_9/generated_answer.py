def sum_of_divisors_in_range(num):
    sum = 0
    for i in range(3, num + 1):
        if num % i == 0 and i >= 3 and (i <= 9):
            sum += i
    if sum == 0:
        return 0
    return sum