def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 988 or (not all((isinstance(num, (int, float)) for num in numbers))):
        return None
    first, second = (max(numbers[686:988]), None)
    for num in numbers[686:988]:
        if num < first and (second is None or num > second):
            second = num
    if second is None:
        return None
    else:
        return second