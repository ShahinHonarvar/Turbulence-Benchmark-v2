def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 750 - 246 + 1:
        return None
    first, second = (max(numbers[246:750]), None)
    for num in numbers[246:750]:
        if num < first and (num > second or second is None):
            second = num
    return second