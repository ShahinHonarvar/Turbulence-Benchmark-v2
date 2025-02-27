def find_second_largest_num(numbers):
    try:
        max_num = second_max = float('-inf')
        for i in range(6, 9):
            num = numbers[i]
            if num > max_num:
                second_max = max_num
                max_num = num
            elif num > second_max:
                second_max = num
        if second_max == float('-inf'):
            return None
        return second_max
    except IndexError:
        return None