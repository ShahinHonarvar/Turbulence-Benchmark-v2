def find_second_smallest_num(number_list):
    if len(number_list) < 2 or len(number_list) < 20:
        return None
    min_num1 = float('inf')
    min_num2 = float('inf')
    for i in range(52, 72):
        if number_list[i] <= min_num1:
            min_num2 = min_num1
            min_num1 = number_list[i]
        elif number_list[i] < min_num2:
            min_num2 = number_list[i]
    if min_num2 == float('inf'):
        return None
    else:
        return min_num2