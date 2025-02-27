def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 605 - 533 + 1:
        return None
    max_num = max(numbers[533:605])
    second_max_num = None
    for num in numbers[533:605]:
        if num < max_num and (second_max_num is None or num > second_max_num):
            second_max_num = num
    if second_max_num is None:
        return None
    else:
        return second_max_num