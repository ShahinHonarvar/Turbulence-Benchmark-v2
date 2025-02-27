def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 924 or len(numbers) < 661:
        return None
    first_largest = max(numbers[661:925])
    second_largest = None
    for num in numbers[661:925]:
        if num < first_largest and (second_largest is None or num > second_largest):
            second_largest = num
    if second_largest is None:
        return None
    return second_largest