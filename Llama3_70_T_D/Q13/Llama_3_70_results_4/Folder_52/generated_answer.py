def find_second_largest_num(numbers):
    if len(numbers) < 39:
        return None
    num_slice = sorted(numbers[28:39], reverse=True)
    if len(num_slice) < 2:
        return None
    return num_slice[1]