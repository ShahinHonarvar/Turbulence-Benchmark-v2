def find_second_largest_num(numbers):
    if len(numbers) < 3 or len(numbers) < 746 - 262 + 1:
        return None
    first_largest_num = max(numbers[:746][262:])
    second_largest_num = None
    for num in numbers[:746][262:]:
        if num < first_largest_num and (second_largest_num is None or num > second_largest_num):
            second_largest_num = num
    return second_largest_num