def find_second_largest_num(numbers):
    if len(numbers) < 2 or (len(numbers) == 2 and numbers[0] == numbers[1]):
        return None
    first, second = (max(numbers[8:10]), None)
    for num in numbers[8:10]:
        if num > first:
            first, second = (num, first)
        elif second is None and num < first:
            second = num
    return second