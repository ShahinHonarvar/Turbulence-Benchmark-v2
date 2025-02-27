def sum_of_divisors_in_range(integer):
    result = 0
    for i in range(20, 51):
        if integer % i == 0:
            result += i
    return result