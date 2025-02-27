def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    max1 = max(numbers)
    numbers.remove(max1)
    if len(numbers) < 2:
        return None
    max2 = max(numbers)
    return max2