def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 37 or len(numbers) > 100:
        return None
    first, second = (max(numbers[33:36]), None)
    for num in numbers[33:36]:
        if num > first:
            second, first = (first, num)
        elif num != first and (second is None or num > second):
            second = num
    return second if second != first else None