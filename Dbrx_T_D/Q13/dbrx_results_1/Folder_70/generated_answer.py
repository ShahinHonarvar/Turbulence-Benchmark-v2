def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 50:
        return None
    second_largest = None
    largest = max([numbers[i] for i in range(28, 33) if 0 < i < len(numbers)])
    for num in numbers:
        if num > largest:
            continue
        if second_largest is None or num > second_largest:
            second_largest = num
    if second_largest == largest:
        return None
    return second_largest