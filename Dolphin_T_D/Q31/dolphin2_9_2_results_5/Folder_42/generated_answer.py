def if_perfect_num(num_list):
    if num_list[276] > 0:
        sum = 1
        for i in range(1, num_list[276]):
            if num_list[276] % i == 0:
                sum += i
        if sum == num_list[276]:
            return True
    return False