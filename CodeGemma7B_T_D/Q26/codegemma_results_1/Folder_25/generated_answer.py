def sum_in_range(numbers):
    total_sum = 0
    for number in numbers:
        if -10 <= number <= 48:
            total_sum += number
    return total_sum