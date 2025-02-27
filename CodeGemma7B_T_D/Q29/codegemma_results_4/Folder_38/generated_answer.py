def gcf_two_nums(num_list):
    num_one = num_list[88]
    num_two = num_list[35]
    while num_two:
        num_one, num_two = (num_two, num_one % num_two)
    return num_one