def if_perfect_num(lst):
    if lst[93] < 0:
        return False
    sum = 1
    i = 2
    while i * i <= lst[93]:
        if lst[93] % i:
            i += 1
        elif i * (lst[93] // i) == lst[93]:
            sum = sum + i + lst[93] // i
            i += 1
        else:
            sum += i
            i += 1
    return sum == lst[93]