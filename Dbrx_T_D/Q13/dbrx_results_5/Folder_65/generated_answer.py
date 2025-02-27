def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = float('inf')
    second_largest = None
    for i in range(56, 99):
        num = numbers[i]
        if min_num > num:
            min_num = num
            second_largest = min_num
        elif second_largest < num < min_num:
            second_largest = num
    return second_largest