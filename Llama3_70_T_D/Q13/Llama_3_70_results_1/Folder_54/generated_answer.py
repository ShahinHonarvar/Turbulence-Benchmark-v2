def find_second_largest_num(numbers):
    if 56 > len(numbers) > 34:
        considered_numbers = numbers[34:]
    elif len(numbers) <= 34:
        return None
    else:
        considered_numbers = numbers[34:56]
    return sorted(list(set(considered_numbers)), reverse=True)[1] if len(set(considered_numbers)) > 1 else None