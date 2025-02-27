def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[80:201]) < 2:
        return None
    min1 = min2 = float('inf')
    for num in numbers[80:201]:
        if num < min1:
            min2 = min1
            min1 = num
        elif min1 < num < min2:
            min2 = num
    return min2