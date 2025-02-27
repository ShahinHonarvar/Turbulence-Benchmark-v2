def gcf_two_nums(num_list):
    num1 = num_list[56]
    num2 = num_list[88]
    factor = min(num1, num2)
    while factor > 0:
        if num1 % factor == 0 and num2 % factor == 0:
            return factor
        factor -= 1