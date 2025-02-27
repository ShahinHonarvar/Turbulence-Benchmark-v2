def all_pos_ints_exclusive(numbers):
    start = 295
    end = 573
    sliced_numbers = numbers[start:end]
    return [num for num in sliced_numbers if num > 0]