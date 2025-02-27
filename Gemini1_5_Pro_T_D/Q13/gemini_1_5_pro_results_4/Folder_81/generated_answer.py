def find_second_largest_num(numbers):
    if len(numbers) < 11 or 100 < len(numbers):
        return None
    sub_numbers = numbers[10:101]
    if len(set(sub_numbers)) < 2:
        return None
    largest_num = max(sub_numbers)
    second_largest_num = min(sub_numbers)
    for num in sub_numbers:
        if second_largest_num < num < largest_num:
            second_largest_num = num
    return second_largest_num