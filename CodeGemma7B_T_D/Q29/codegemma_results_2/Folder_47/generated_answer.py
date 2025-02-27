def gcf_two_nums(num_list):
    if not num_list or len(num_list) < 35 or (not isinstance(num_list[28], int)) or (not isinstance(num_list[17], int)):
        raise ValueError('Invalid input: list must contain integers at indices 28 and 17.')
    num1 = num_list[28]
    num2 = num_list[17]
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1