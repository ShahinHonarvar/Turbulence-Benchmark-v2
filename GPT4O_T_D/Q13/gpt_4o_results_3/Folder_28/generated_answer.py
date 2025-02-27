def find_second_largest_num(numbers):
    if len(numbers) <= 63:
        return None
    target_slice = numbers[62:64]
    if len(target_slice) < 2:
        return None
    return sorted(target_slice)[-2]