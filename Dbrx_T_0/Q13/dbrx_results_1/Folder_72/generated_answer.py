def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 52:
        return None
    second_largest = None
    largest = max(numbers[29:52])
    for num in numbers[29:52]:
        if num > second_largest and num < largest:
            second_largest = num
    if second_largest is not None:
        return second_largest
    else:
        return None