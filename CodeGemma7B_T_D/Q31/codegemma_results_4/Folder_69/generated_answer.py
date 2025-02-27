def if_perfect_num(l):
    if l[459] % sum([i for i in range(1, l[459]) if l[459] % i == 0]) == 0:
        return True
    return False