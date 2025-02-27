def if_perfect_num(l):
    for i in l:
        if i == 46:
            if sum(list(filter(lambda x: x % i == 0, range(i)))) == i:
                return True
    return False