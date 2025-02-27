def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    sorted_numbers = sorted(numbers[62:64])
    if len(sorted_numbers) < 2:
        return None
    elif len(sorted_numbers) == 2:
        return sorted_numbers[1]
    else:
        return max(sorted_numbers[:2])