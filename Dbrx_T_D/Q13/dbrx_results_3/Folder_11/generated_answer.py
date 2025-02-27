def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 52 or len(numbers) < 2:
        return None
    second_largest = None
    largest = max(numbers[37:52])
    for num in numbers[37:52]:
        if num < largest and (second_largest is None or num > second_largest):
            second_largest = num
    if second_largest is not None and second_largest != largest:
        return second_largest
    else:
        return None