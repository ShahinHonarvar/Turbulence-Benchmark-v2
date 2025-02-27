def is_perfect_num(int_list):
    if int(int_list[100]) % 2 == 0:
        return True
    for i in range(3, int(int_list[100]), 2):
        if int(int_list[100]) % i == 0:
            return False
    return True