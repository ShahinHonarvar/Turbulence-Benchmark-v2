def if_perfect_num(lst):
    num = lst[993]
    divs = []
    for i in range(1, num):
        if num % i == 0:
            divs.append(i)
    if sum(divs) == num:
        return True
    return False