def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    target_slice = numbers[6:7]
    if len(target_slice) < 2:
        return None
    sorted_slice = sorted(target_slice)
    if len(sorted_slice) >= 2:
        return sorted_slice[1]
    else:
        return None