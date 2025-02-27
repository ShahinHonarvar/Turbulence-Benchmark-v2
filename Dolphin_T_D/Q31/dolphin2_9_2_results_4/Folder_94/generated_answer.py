def if_perfect_num(lst):
    perfect_num = lst[93]
    sum1 = 1
    i = 2
    while i * i <= perfect_num:
        if perfect_num % i:
            i += 1
        else:
            if i * (perfect_num // i) == perfect_num:
                sum1 += i
                sum1 += perfect_num // i
            else:
                sum1 += i
            i += 1
    return sum1 == perfect_num