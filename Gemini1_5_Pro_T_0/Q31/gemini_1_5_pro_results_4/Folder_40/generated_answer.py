def if_perfect_num(l):
    sum = 1
    for i in range(2, int(l[7] ** 0.5) + 1):
        if l[7] % i == 0:
            sum += i + l[7] // i
    if sum == l[7]:
        return True
    else:
        return False