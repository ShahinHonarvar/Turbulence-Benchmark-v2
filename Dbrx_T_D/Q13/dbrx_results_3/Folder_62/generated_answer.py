def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 2 < 91 or len(numbers) - 2 > 99:
        return None
    first, second = (max(numbers[91:99]), None)
    for num in numbers[91:99]:
        if num < first and (second is None or num > second):
            second = num
    return second