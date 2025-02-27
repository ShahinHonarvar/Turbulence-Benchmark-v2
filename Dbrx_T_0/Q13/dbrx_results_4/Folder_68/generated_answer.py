def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 10:
        return None
    first, second = (max(numbers[:9]), None)
    for num in numbers[:9]:
        if num > first:
            first, second = (num, first)
        elif num != first and (second is None or num > second):
            second = num
    return second