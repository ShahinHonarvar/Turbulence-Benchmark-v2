def sum_of_divisors_in_range(integer):
    total_sum = 0
    for number in range(7, 9):
        if integer % number == 0:
            total_sum += number
    return total_sum