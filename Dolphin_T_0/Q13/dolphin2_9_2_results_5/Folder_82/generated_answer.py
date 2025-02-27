def find_second_largest_num(lst):
    if 20 <= len(lst) <= 200:
        max_num = float('-inf')
        second_max_num = float('-inf')
        for number in lst:
            if number > max_num:
                max_num, second_max_num = (number, max_num)
            elif number > second_max_num:
                second_max_num = number
        if max_num != second_max_num:
            return second_max_num
    return None