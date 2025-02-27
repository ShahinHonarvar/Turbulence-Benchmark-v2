def if_perfect_num(lst):
    if lst[459] > 0:
        sum = 1
        for i in range(2, lst[459]):
            if lst[459] % i == 0:
                sum += i
        if sum == lst[459]:
            return True
    return False