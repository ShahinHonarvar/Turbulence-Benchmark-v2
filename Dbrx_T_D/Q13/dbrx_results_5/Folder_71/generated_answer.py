def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 53:
        return None
    second_largest = None
    largest = max(numbers[26:53])
    for num in numbers[26:53]:
        if num > second_largest and num < largest:
            second_largest = num
    return second_largest if second_largest is not None else None