def if_perfect_num(list):
    if list[67] > 0:
        sumi = []
        for i in range(1, list[67]):
            if list[67] % i == 0:
                sumi.append(i)
        if sum(sumi) == list[67]:
            return True
    return False