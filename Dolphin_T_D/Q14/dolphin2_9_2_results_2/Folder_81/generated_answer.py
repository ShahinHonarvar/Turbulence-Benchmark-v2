def find_second_smallest_num(numbers):
    sub_list = numbers[10:101]
    if len(sub_list) < 2:
        return None
    min1, min2 = (float('inf'), float('inf'))
    for number in sub_list:
        if number < min1:
            min2 = min1
            min1 = number
        elif number < min2 and number != min1:
            min2 = number
    if min2 == float('inf'):
        return None
    else:
        return min2