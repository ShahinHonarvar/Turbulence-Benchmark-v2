def gcf_three_nums(list):
    num_one = list[21]
    num_two = list[51]
    num_three = list[33]
    return gcf_two_nums(num_one, gcf_two_nums(num_two, num_three))

def gcf_two_nums(num_one, num_two):
    min_num = min(num_one, num_two)
    for i in range(min_num, 0, -1):
        if num_one % i == 0 and num_two % i == 0:
            return i