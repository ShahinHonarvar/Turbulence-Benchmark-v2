def if_perfect_num(int_list):
    if int_list[714] > 0:
        div_sum = 0
        for i in range(1, int_list[714]):
            if int_list[714] % i == 0:
                div_sum += i
        if div_sum == int_list[714]:
            return True
    return False