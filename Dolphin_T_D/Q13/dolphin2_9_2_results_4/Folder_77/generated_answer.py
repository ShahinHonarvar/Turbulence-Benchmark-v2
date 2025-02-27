def find_second_largest_num(numbers):
    if not numbers:
        return None
    if len(numbers) < 2:
        return None
    maximum = second_maximum = float('-inf')
    for num in numbers:
        if num > maximum:
            second_maximum = maximum
            maximum = num
        elif num > second_maximum and num != maximum:
            second_maximum = num
    return second_maximum if second_maximum != float('-inf') else None