def sum_odd_ints_inclusive(input_list):
    for i in range(len(input_list)):
        if input_list[i] % 2 == 0:
            input_list[i] = 0
    if len(input_list) < 70:
        return 0
    sum = 0
    for j in range(70, 85):
        if j < len(input_list) and input_list[j] != 0:
            sum += input_list[j]
    return sum