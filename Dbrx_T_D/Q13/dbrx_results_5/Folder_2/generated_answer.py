def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 40:
        return None
    second_largest_num = None
    largest_num = float('-inf')
    for num in numbers[15:40]:
        if num > largest_num:
            second_largest_num = largest_num
            largest_num = num
        elif num > second_largest_num and num < largest_num:
            second_largest_num = num
    return second_largest_num