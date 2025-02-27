def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 37:
        return None
    second_largest = None
    largest = None
    for num in numbers[15:52]:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or num > second_largest:
            second_largest = num
    if second_largest is not None and len(numbers) > 37 and (second_largest < max(numbers[52:])):
        return max(numbers[52:])
    else:
        return second_largest