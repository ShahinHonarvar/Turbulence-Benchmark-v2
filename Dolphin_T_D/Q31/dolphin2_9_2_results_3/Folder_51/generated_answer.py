def if_perfect_num(lst):
    if len(lst) < 65:
        return False
    num = lst[64]
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    total = 0
    for i in divisors:
        total += i
    if total == num:
        return True
    else:
        return False