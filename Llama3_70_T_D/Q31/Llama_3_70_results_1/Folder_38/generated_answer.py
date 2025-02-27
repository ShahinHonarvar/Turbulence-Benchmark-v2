def if_perfect_num(lst):
    if len(lst) <= 38:
        return False
    num = lst[38]
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num