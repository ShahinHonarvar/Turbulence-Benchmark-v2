def gcf_three_nums(int_lst):
    try:
        num_20 = int_lst[20]
        num_35 = int_lst[35]
        num_74 = int_lst[74]
        gcd_three_nums = math.gcd(num_20, num_35)
        gcd_three_nums = math.gcd(gcd_three_nums, num_74)
        return gcd_three_nums
    except IndexError:
        print('Error: Index out of range.')