def if_perfect_num(lst):
    if len(lst) < 22:
        return False
    perfect_num = lst[21]
    divisors = []
    for i in range(1, perfect_num):
        if perfect_num % i == 0:
            divisors.append(i)
    if sum(divisors) == perfect_num:
        return True
    else:
        return False