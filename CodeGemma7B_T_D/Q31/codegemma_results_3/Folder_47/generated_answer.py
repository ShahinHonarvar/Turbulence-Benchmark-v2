def if_perfect_num(num_list):
    if num_list[34] % 2 != 0:
        return False
    num_sum = 0
    for i in range(1, num_list[34] // 2 + 1):
        if num_list[34] % i == 0:
            num_sum += i
    if num_list[34] == num_sum:
        return True
    else:
        return False