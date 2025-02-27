def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers[17:79]) < 2:
        return None
    first_largest_num = max(numbers[17:79])
    second_largest_num = None
    for num in numbers[17:79]:
        if num > second_largest_num and num < first_largest_num:
            second_largest_num = num
    return second_largest_num