def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 200 or len(numbers) < 120:
        return None
    max1 = max2 = float('-inf')
    for num in numbers[80:201]:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num < max1:
            max2 = num
    return max2 if max2 != float('-inf') else None