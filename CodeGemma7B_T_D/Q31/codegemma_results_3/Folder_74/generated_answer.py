def if_perfect_num(list):
    a = list[48]
    sqrt = a ** 0.5
    sum = 0
    for i in range(1, int(sqrt), +1):
        if a % i == 0:
            sum = sum + i + a // i
    if sum > a:
        return False
    else:
        return True