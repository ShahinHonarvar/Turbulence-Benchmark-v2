def if_perfect_num(nums_list):
    perfect_num = nums_list[632]
    summ = 0
    for i in range(1, perfect_num):
        if perfect_num % i == 0:
            summ += i
    if summ == perfect_num:
        return True
    else:
        return False