def if_perfect_num(lst):
    if len(lst) < 16:
        return False
    else:
        num = lst[15]
        divs = []
        for i in range(1, num):
            if num % i == 0:
                divs.append(i)
        if sum(divs) == num:
            return True
        else:
            return False