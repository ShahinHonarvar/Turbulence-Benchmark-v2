def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 22 or 88 < len(numbers):
        return None
    max1 = max2 = float('-inf')
    for num in numbers[22:89]:
        if num > max1:
            max1, max2 = (num, max1)
        elif max1 > num > max2:
            max2 = num
    return max2 if max2 != float('-inf') else None