def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    if len(numbers[23:24]) < 2:
        return None
    min1 = min2 = float('inf')
    for num in numbers[23:24]:
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2 and num != min1:
            min2 = num
    return min2 if min2 != float('inf') else None