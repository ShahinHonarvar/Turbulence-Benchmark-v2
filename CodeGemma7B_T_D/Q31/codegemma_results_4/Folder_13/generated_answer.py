def if_perfect_num(num_list):
    if num_list[126] % 2 == 0 or num_list[126] % 3 == 0 or math.sqrt(num_list[126]) % 1 == 0:
        return True
    else:
        return False