def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 86 or max(numbers) == min(numbers):
        return None
    first_largest = max(numbers[75:86])
    second_largest = None
    for num in numbers[75:86]:
        if num < first_largest and (not second_largest or num > second_largest):
            second_largest = num
    if not second_largest:
        return None
    return second_largest