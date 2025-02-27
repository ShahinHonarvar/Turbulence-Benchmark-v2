def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 53:
        return None
    second_largest = None
    largest = max(numbers[25:53])
    for num in numbers[25:53]:
        if num < largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest