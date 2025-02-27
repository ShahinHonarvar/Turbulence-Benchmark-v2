def find_second_largest_num(numbers):
    if len(numbers) < 3 or len(numbers) - 1 < 66 or 64 > len(numbers) - 2:
        return None
    second_largest = None
    largest = max(numbers[64:67])
    for num in numbers[64:67]:
        if num < largest and (second_largest is None or num > second_largest):
            second_largest = num
    if second_largest is None:
        for num in numbers[:64] + numbers[67:]:
            if num > largest:
                return None
            if second_largest is None or num > second_largest:
                second_largest = num
    return second_largest