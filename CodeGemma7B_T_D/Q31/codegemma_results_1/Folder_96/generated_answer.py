def if_perfect_num(num_list):
    if num_list[47] > 1:
        for i in range(2, num_list[47]):
            if num_list[47] % i == 0:
                return False
        return True
    return False