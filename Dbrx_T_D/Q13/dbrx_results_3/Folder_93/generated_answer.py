def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 95:
        return None
    numbers = numbers[74:95]
    first_largest = max(numbers[:2])
    second_largest = min(first_largest, numbers[-1])
    for num in numbers[2:]:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num < first_largest:
            second_largest = num
    if second_largest == first_largest:
        return None
    else:
        return second_largest