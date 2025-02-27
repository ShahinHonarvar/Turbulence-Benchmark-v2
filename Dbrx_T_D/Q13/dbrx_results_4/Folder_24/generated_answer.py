def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 95 - 74 + 1:
        return None
    first_largest_num = max(numbers[74:96])
    second_largest_num = None
    for num in numbers[74:96]:
        if num < first_largest_num and (second_largest_num is None or num > second_largest_num):
            second_largest_num = num
    if second_largest_num is None:
        return None
    else:
        return second_largest_num