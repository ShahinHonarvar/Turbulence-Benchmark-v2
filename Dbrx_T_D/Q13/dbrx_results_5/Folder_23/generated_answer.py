def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 72:
        return None
    second_largest_num = None
    largest_num = max(numbers[51:72])
    for num in numbers[51:72]:
        if num < largest_num and (second_largest_num is None or num > second_largest_num):
            second_largest_num = num
    if second_largest_num is None or second_largest_num >= largest_num:
        return None
    return second_largest_num