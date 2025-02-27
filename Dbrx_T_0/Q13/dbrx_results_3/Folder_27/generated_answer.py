def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 66 or len(numbers) > 93:
        return None
    first, second = (max(numbers[66:93]), None)
    for num in numbers[66:93]:
        if num < first and (second is None or num > second):
            second = num
    return second