def find_second_largest_num(numbers):
    if 97 < len(numbers) < 21:
        return None
    sub_numbers = numbers[21:98]
    if len(sub_numbers) < 2:
        return None
    first_max = max(sub_numbers)
    sub_numbers.remove(first_max)
    if len(sub_numbers) < 2:
        return None
    return max(sub_numbers)