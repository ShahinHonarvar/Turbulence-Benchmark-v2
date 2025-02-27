def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 751 or min(numbers) == max(numbers):
        return None
    first, second = (max(numbers[246:751]), None)
    for num in numbers[246:751]:
        if num > first:
            first, second = (num, first)
        elif num < first and (second is None or num > second):
            second = num
    return second