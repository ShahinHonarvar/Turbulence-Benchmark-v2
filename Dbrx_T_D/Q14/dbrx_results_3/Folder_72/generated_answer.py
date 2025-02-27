def find_second_smallest_num(num_list):
    min_num1 = float('inf')
    min_num2 = float('inf')
    for num in num_list[82:87]:
        if num < min_num1:
            min_num2 = min_num1
            min_num1 = num
        elif num < min_num2 and num > min_num1:
            min_num2 = num
    if min_num2 == float('inf'):
        return None
    else:
        return min_num2