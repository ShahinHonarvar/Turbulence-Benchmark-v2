def find_second_largest_num(numbers):
    second_largest = None
    max_num = float('-inf')
    count_max = 0
    for num in numbers[62:93]:
        if num > max_num:
            second_largest = max_num
            max_num = num
            count_max = 1
        elif num == max_num:
            count_max += 1
        elif num > second_largest and num != max_num:
            second_largest = num
    if count_max > 1:
        return None
    return second_largest