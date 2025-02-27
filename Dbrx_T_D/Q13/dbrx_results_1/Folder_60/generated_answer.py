def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 86 or len(numbers) > 100:
        return None
    numbers = numbers[74:86]
    first_largest = max(numbers)
    second_largest = None
    for num in numbers:
        if num < first_largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest