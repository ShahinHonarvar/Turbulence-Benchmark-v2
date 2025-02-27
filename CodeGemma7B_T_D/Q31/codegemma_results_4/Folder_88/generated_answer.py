def if_perfect_num(li):
    if li[46] >= 6 and sum((i for i in range(1, li[46] + 1) if li[46] % i == 0)) == li[46]:
        return True
    else:
        return False