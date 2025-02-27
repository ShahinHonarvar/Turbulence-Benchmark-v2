def find_second_smallest_num(numbers):
    numbers_in_range = numbers[1:101]
    numbers_in_range.sort()
    if len(numbers_in_range) < 2:
        return None
    return numbers_in_range[1]