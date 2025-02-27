def if_perfect_num(num_list):
    num = num_list[15]
    perfect_num = 0
    for i in range(1, num + 1):
        if num % i == 0:
            perfect_num += i
    return perfect_num == num