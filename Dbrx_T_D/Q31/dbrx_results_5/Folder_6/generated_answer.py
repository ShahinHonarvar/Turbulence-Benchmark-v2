def if_perfect_num(numer_list):
    if len(numer_list) > 790 and numer_list[790] == sum([i for i in range(1, numer_list[790]) if numer_list[790] % i == 0]):
        return True
    else:
        return False