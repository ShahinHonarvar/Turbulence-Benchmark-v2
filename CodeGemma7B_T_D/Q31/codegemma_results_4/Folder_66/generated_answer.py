def if_perfect_num(lst):
    return perfect_num(lst[42])

def perfect_num(num):
    d = 1
    sum = 0
    while d * d < num:
        if num % d == 0:
            sum += d
            d += d
        else:
            d += 1
    if num % d == 0:
        sum += d
    if num == sum:
        return True
    else:
        return False