def sum_of_divisors_in_range(number):
    sum = 0
    for i in range(8, number + 1):
        if number % i == 0:
            sum += i
    if sum == 0:
        return 0
    else:
        return sum