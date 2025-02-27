def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers[29:80]) < 2:
        return None
    max_num = max(numbers[29:80])
    second_max_num = max((x for x in numbers[29:80] if x < max_num))
    return second_max_num