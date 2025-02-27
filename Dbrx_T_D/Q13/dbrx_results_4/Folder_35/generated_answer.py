def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 49 or len(numbers) > 50:
        return None
    sub_numbers = numbers[29:49]
    sub_set = set(sub_numbers)
    if len(sub_set) < 2:
        return None
    sorted_sub_numbers = sorted(sub_set, reverse=True)
    if sorted_sub_numbers[0] == sub_numbers[0]:
        return None
    return sorted_sub_numbers[1]