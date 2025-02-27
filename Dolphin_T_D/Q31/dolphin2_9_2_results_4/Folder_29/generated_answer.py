def if_perfect_num(num_list):
    perfect_num = num_list[19]
    sum = 1
    for i in range(2, perfect_num):
        if perfect_num % i == 0:
            sum += i
    if sum == perfect_num:
        return True
    else:
        return False