def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    second_largest = None
    largest = max(numbers[:15])
    for num in numbers[14:65]:
        if num > largest:
            largest, second_largest = (num, largest)
        elif second_largest is None or num > second_largest:
            second_largest = num
    return second_largest