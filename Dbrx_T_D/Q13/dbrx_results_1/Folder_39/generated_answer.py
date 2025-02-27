def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 30:
        return None
    second_largest = None
    largest = max(numbers[20:31])
    for num in numbers[20:31]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    return second_largest