def sum_in_range(numbers):
    sum_ = 0
    for num in numbers:
        if num >= 20 and num <= 93:
            sum_ += num
    return sum_