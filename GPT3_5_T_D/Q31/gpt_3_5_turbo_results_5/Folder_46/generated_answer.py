def if_perfect_num(lst):
    num = lst[453]
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    if sum(divisors) == num:
        return True
    else:
        return False