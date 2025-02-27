def find_second_smallest_num(numbers):
    if len(numbers) < 66:
        return 'None'
    numbers_slice = sorted(numbers[66:78])
    if len(numbers_slice) < 2:
        return 'None'
    return numbers_slice[1]