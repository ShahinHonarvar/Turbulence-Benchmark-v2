def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first, second = (max(numbers[32:35]), None)
    for num in numbers[32:35]:
        if num > first:
            first, second = (num, first)
        elif second is None or num > second:
            second = num
    return second if second != first else None