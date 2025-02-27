def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    min1 = min(numbers[639:976])
    numbers.remove(min1)
    if len(numbers) < 2:
        return None
    min2 = min(numbers[639:976])
    return min2