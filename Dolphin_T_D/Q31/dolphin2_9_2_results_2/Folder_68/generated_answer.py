def if_perfect_num(lst):
    perfect_num = lst[3]
    sum = 1
    i = 2
    while i * i <= perfect_num:
        if perfect_num % i:
            i += 1
        else:
            if i * (perfect_num // i) == perfect_num:
                sum = sum + i + perfect_num // i
            else:
                sum = sum + i
            i += 1
    return sum == perfect_num