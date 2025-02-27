def find_second_largest_num(numbers):
    if len(numbers) < 2 or (len(numbers) == 2 and numbers[0] == numbers[1]):
        return None
    first_largest_num = max(numbers[:9])
    second_largest_num = None
    for num in numbers[:9]:
        if num < first_largest_num and (second_largest_num is None or num > second_largest_num):
            second_largest_num = num
    return second_largest_num