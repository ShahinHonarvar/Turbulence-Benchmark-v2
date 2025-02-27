def if_perfect_num(int_list):
    if int_list[49] % 2 == 0 or int_list[49] == 1:
        return False
    sum = 1
    for i in range(2, int_list[49] // 2 + 1):
        if int_list[49] % i == 0:
            sum += i
    if sum == int_list[49]:
        return True
    else:
        return False