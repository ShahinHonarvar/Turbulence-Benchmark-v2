def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 41 or len(numbers) > 81:
        return None
    max1 = max(max(numbers[:40]), max(numbers[80:]))
    max2 = None
    for num in numbers[41:79]:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num < max1:
            max2 = num
    return max2