def find_second_largest_num(lst):
    if len(lst) >= 2:
        first = second = float('-inf')
        for num in lst:
            if num > first:
                first, second = (num, first)
            elif first > num > second:
                second = num
        if second != float('-inf'):
            return second
    return None