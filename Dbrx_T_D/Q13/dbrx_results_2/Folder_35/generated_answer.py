def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = float('inf')
    second_num = float('-inf')
    for i in range(30, 49):
        num = numbers[i]
        if num > min_num:
            if num > second_num:
                second_num = num
            elif num < second_num:
                min_num, second_num = (num, min_num)
    return second_num if second_num != float('-inf') else None