def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 200 or len(numbers) < 40:
        return None
    numbers = numbers[40:201]
    numbers.sort(reverse=True)
    first, second = (None, None)
    for num in numbers:
        if first is None or num > first:
            second = first
            first = num
        elif second is None or num > second:
            second = num
    if second is not None and second != first:
        return second
    else:
        return None