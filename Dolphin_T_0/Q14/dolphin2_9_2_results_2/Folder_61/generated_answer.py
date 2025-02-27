def find_second_smallest_num(numbers):
    if len(numbers) < 8:
        return None
    min1 = min(numbers[0:8])
    if numbers.count(min1) == 1:
        numbers.remove(min1)
    else:
        return None
    min2 = min(numbers[0:8])
    return min2