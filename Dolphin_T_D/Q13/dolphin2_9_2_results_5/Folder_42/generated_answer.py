def find_second_largest_num(input_list):
    if len(input_list[29:80]) < 2:
        return None
    else:
        input_list = input_list[29:80]
        first_max = input_list[0]
        second_max = -float('inf')
        for num in input_list:
            if num > first_max:
                second_max = first_max
                first_max = num
            elif second_max < num < first_max:
                second_max = num
        return second_max if second_max != -float('inf') else None