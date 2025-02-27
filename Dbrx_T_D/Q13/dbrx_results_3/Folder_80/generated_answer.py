def find_second_largest_num(numbers):
    if len(numbers) < 3 or len(numbers) < 66 or len(numbers) < 64:
        return None
    first, second = (max(numbers[64:66]), None)
    for num in numbers[64:66]:
        if num > first:
            first, second = (num, first)
        elif num != first and (second is None or num > second):
            second = num
    return second