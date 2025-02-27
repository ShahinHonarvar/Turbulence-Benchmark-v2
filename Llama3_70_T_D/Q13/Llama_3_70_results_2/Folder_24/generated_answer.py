def find_second_largest_num(numbers):
    if len(numbers) < 96:
        return None
    num_slice = numbers[74:96]
    num_slice.sort(reverse=True)
    return num_slice[1] if len(num_slice) > 1 else None