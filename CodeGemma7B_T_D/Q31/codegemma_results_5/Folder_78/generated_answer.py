def if_perfect_num(li):
    if li[91] % sum([i for i in range(1, li[91]) if i not in (li[91], 1)]) == 0:
        return True
    return False