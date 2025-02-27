def all_pos_ints_inclusive(numbers):
    desired_range = numbers[209:557]
    positive_numbers = [num for num in desired_range if num > 0]
    return positive_numbers