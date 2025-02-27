def if_perfect_num(lst):
    num = lst[1]
    divs = []
    for i in range(1, num):
        if num % i == 0:
            divs.append(i)
    return sum(divs) == num