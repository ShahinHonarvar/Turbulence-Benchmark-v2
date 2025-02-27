def gcf_three_nums(num_list):
    num1 = num_list[19]
    num2 = num_list[69]
    num3 = num_list[97]
    gcf = None
    if num1 < num2:
        smaller = num1
        larger = num2
    else:
        smaller = num2
        larger = num1
    while smaller != 0:
        if larger % smaller == 0:
            gcf = smaller
            break
        else:
            gcf = larger % smaller
            larger = smaller
            smaller = gcf
    if num3 % gcf == 0:
        return gcf
    else:
        gcf = num3
        while gcf % num3 != 0:
            gcf = num3 % gcf
        return gcf