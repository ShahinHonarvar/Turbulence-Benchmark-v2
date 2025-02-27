def find_second_largest_num(numbers):
    if len(numbers) < 2 or 23 >= len(numbers) or 23 < 0:
        return None
    sub_numbers = numbers[23:24]
    if len(sub_numbers) < 2:
        return None
    largest_num = max(sub_numbers)
    sub_numbers.remove(largest_num)
    return max(sub_numbers)