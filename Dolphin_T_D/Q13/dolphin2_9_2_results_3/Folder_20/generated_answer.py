def find_second_largest_num(numbers):
    if not numbers:
        return None
    if len(numbers) == 1:
        return None
    max1 = max(numbers)
    numbers_without_max = [num for num in numbers if num != max1]
    if not numbers_without_max:
        return None
    max2 = max(numbers_without_max)
    return max2