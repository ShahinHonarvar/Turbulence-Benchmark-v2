def if_perfect_num(lst):
    if len(lst) < 21:
        return False
    num = lst[20]
    divs = []
    i = 1
    while i * i <= num:
        if num % i == 0:
            divs.append(i)
            if i != num // i:
                divs.append(num // i)
        i += 1
    return sum(divs) == num and len(divs) != 1