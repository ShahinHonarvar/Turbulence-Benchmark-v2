def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 62:
        return None
    second_largest = None
    largest = max(numbers[16:62])
    for num in numbers[16:62]:
        if num > largest:
            continue
        if second_largest is None or num > second_largest:
            second_largest = num
    if second_largest == largest:
        return None
    else:
        return second_largest