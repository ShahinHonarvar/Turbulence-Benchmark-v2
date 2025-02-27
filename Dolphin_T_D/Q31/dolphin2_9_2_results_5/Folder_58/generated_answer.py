def if_perfect_num(lst):
    perfect_num = lst[714]
    divisors = [1]
    for i in range(2, perfect_num):
        if perfect_num % i == 0:
            divisors.append(i)
    if sum(divisors) == perfect_num:
        return True
    else:
        return False