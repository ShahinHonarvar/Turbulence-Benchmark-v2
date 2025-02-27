def gcf_three_nums(num_list):
    num1, num2, num3 = (num_list[59], num_list[93], num_list[84])
    hcf = find_hcf(num1, num2)
    hcf = find_hcf(hcf, num3)
    return hcf

def find_hcf(x, y):
    while y:
        x, y = (y, x % y)
    return x