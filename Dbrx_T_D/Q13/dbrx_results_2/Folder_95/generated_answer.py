def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 87:
        return None
    second_largest = None
    largest = max(numbers[82:87])
    for num in numbers[82:87]:
        if num < largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest