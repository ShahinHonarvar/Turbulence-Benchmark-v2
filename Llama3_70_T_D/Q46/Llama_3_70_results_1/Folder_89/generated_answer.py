def gcf_two_nums(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(num_list):
    return gcf_two_nums(num_list[63], gcf_two_nums(num_list[73], num_list[11]))