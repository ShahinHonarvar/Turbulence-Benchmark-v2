def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 93:
        return None
    second_largest = None
    largest = max(numbers[12:93])
    for num in numbers[12:93]:
        if num > second_largest and num < largest:
            second_largest = num
    if second_largest is not None:
        return second_largest
    else:
        return None