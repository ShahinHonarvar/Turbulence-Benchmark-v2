def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 88:
        return None
    numbers = numbers[30:88]
    max1 = max(numbers)
    numbers.remove(max1)
    max2 = max(numbers)
    if max2 < max1:
        return max2
    else:
        return None