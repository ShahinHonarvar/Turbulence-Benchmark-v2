def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 98 - 55 + 1:
        return None
    numbers = numbers[55:99]
    unique_numbers = set(numbers)
    if len(unique_numbers) < 2:
        return None
    first, second = (max(unique_numbers), float('-inf'))
    for num in unique_numbers:
        if num > first:
            first, second = (num, first)
        elif num > second and num < first:
            second = num
    return second