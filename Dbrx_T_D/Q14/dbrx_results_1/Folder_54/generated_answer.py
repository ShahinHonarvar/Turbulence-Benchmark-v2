def find_second_smallest_num(numbers):
    if len(numbers) < 2 or (len(numbers) >= 86 - 68 + 1 and len(numbers) < 88):
        return None
    first, second = (min(numbers[68:86]), float('inf'))
    for num in numbers[68:86]:
        if num < second and num > first:
            second = num
    return first if second == float('inf') else second