def find_second_largest_num(numbers):
    numbers_slice = numbers[82:87]
    numbers_slice.sort(reverse=True)
    if len(numbers_slice) < 2:
        return None
    else:
        return numbers_slice[1]