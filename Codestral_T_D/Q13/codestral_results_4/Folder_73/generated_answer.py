def find_second_largest_num(numbers):
    subset = numbers[19:93]
    if len(subset) < 2:
        return None
    else:
        max_num = second_max_num = float('-inf')
        for num in subset:
            if num > max_num:
                second_max_num = max_num
                max_num = num
            elif max_num > num > second_max_num:
                second_max_num = num
        return second_max_num if second_max_num != float('-inf') else None