def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    max_one, max_two = (None, None)
    for num in numbers[13:69]:
        if max_one is None or num > max_one:
            max_two = max_one
            max_one = num
        elif max_two is None or num > max_two:
            max_two = num
    return max_two