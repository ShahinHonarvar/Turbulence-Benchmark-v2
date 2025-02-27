def find_second_smallest_num(numbers):
    numbers_slice = numbers[80:201]
    if len(numbers_slice) < 2:
        return None
    numbers_slice.sort()
    return numbers_slice[1]