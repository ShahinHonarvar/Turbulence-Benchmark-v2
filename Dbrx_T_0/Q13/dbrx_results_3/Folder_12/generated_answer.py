def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 65:
        return None
    second_largest = None
    largest = max(numbers[14:65])
    for num in numbers[14:65]:
        if num > second_largest and num < largest:
            second_largest = num
    return second_largest