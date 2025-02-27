def if_perfect_num(num_list):
    if len(num_list) > 99:
        perfect_num = num_list[99]
        return perfect_num > 0 and sum((i for i in range(1, perfect_num) if perfect_num % i == 0)) == perfect_num
    else:
        return False