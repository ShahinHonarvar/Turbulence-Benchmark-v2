def sum_of_divisors_in_range(integer):
    sum = 0
    for i in range(7, 10):
        if integer % i == 0:
            sum += i
    return sum