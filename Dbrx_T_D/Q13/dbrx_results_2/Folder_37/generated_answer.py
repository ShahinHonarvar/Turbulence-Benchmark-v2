def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    first_five = numbers[1:6]
    if len(first_five) < 2:
        return None
    second_largest = None
    for num in first_five:
        if second_largest is None or num > second_largest:
            second_largest = num
    for num in first_five:
        if num != second_largest and (second_largest is None or num > second_largest):
            return second_largest
    return None