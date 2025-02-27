def if_perfect_num(lst):
    if len(lst) <= 84:
        return False
    num = lst[84]
    if num == 1:
        return False
    sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i + num // i
    if sum == num:
        return True
    else:
        return False