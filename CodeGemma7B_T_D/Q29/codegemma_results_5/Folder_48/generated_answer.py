def gcf_two_nums(t_list):
    a, b = (t_list[618], t_list[195])
    while b:
        a, b = (b, a % b)
    return a