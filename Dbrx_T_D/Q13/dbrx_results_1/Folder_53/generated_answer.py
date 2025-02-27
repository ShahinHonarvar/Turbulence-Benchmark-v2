def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 200 or len(numbers[100:200]) < 2:
        return None
    first, second = (None, None)
    for num in numbers[100:200]:
        if first is None or num > first:
            second = first
            first = num
        elif second is None or num > second:
            second = num
    return second