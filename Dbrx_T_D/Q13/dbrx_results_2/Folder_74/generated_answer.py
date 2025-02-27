def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 78 - 17 + 1:
        return None
    first_largest = None
    second_largest = None
    for i in range(17, 78 + 1):
        num = numbers[i]
        if first_largest is None or num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num < first_largest:
            second_largest = num
    return second_largest