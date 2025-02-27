def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first_largest = max(numbers[55:66])
    second_largest = None
    for num in numbers[55:66]:
        if num < first_largest and (second_largest is None or num > second_largest):
            second_largest = num
    if second_largest is None or first_largest == second_largest:
        return None
    return second_largest