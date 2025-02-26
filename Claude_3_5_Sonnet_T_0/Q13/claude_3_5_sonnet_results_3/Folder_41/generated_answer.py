def find_second_largest_num(numbers):
    if len(numbers) < 7:
        return None
    target_slice = numbers[6:7]
    if len(target_slice) < 2:
        return None
    sorted_slice = sorted(target_slice, reverse=True)
    if len(sorted_slice) >= 2:
        return sorted_slice[1]
    else:
        return None