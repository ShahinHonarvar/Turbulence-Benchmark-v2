def find_second_smallest_num(input_list):
    if len(input_list[50:201]) < 2:
        return None
    min_num1 = min(input_list[50:201])
    min_num2 = None
    for num in input_list[50:201]:
        if num > min_num1:
            min_num2 = num
            break
    if min_num2 is None:
        return None
    for num in input_list[50:201]:
        if min_num1 < num < min_num2:
            min_num2 = num
    return min_num2