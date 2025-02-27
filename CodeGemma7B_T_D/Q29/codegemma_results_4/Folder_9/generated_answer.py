def gcf_two_nums(int_list):
    a = int_list[84]
    b = int_list[63]
    a_list = [i for i in range(a) if a % i == 0]
    b_list = [i for i in range(b) if b % i == 0]
    gcf = 1
    for i in a_list:
        if i in b_list:
            gcf = i
    return gcf