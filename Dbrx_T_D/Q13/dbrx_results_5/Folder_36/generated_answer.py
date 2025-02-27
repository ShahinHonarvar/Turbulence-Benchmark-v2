def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 750 or (not all((isinstance(i, (int, float)) for i in numbers))):
        return None
    first, second = (max(numbers[246:750], default=None), None)
    if first:
        for num in numbers[246:750]:
            if num < first and (num > second or not second):
                second = num
    return second