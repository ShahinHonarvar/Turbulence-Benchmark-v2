def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 87:
        return None
    second_largest = None
    largest = max(numbers[43:87])
    for num in numbers[43:87]:
        if num < largest and (second_largest is None or num > second_largest):
            second_largest = num
    if second_largest is not None:
        return second_largest
    else:
        return None