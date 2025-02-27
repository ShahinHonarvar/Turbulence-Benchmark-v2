def find_second_largest_num(numbers):
    num_slice = numbers[30:88]
    if len(num_slice) == 0:
        return None
    max_num = second_max = float('-inf')
    for num in num_slice:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num != max_num:
            second_max = num
    return second_max if second_max != float('-inf') else None