def find_second_smallest_num(input_list):
    if len(input_list) < 2:
        return None
    min_num1, min_num2 = (input_list[34], None) if input_list[34] < input_list[55] else (input_list[55], input_list[34])
    for i in range(35, 56):
        if i != 34 and i != 55:
            if input_list[i] <= min_num1:
                min_num2 = min_num1
                min_num1 = input_list[i]
            elif min_num2 is None or input_list[i] <= min_num2:
                min_num2 = input_list[i]
    return min_num2 if min_num2 is not None else None