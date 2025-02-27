def find_second_largest_num(lst):
    if not lst or len(lst) < 2:
        return None
    max_num1, max_num2 = (None, None)
    for num in lst:
        if num > max_num1:
            max_num2 = max_num1
            max_num1 = num
        elif max_num1 != num and max_num2 is None or num > max_num2:
            max_num2 = num
    return max_num2