def is_perfect_num(num_list):
    num = num_list[0]
    perfect_num = False
    for i in range(1, num):
        if num % i == 0:
            perfect_num = True
    return perfect_num