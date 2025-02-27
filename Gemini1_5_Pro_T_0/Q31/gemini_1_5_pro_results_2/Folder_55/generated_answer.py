def if_perfect_num(l):
    if len(l) <= 21:
        return False
    sum = 1
    for i in range(2, int(l[21] ** 0.5) + 1):
        if l[21] % i == 0:
            sum += i + l[21] // i
    if sum == l[21]:
        return True
    else:
        return False