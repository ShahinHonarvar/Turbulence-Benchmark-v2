def find_second_largest_num(numbers):
    if 23 < len(numbers) - 1:
        num_slice = numbers[23:]
        num_slice.sort(reverse=True)
        return num_slice[1]
    else:
        return None