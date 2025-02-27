def if_perfect_num(lst):
    num = lst[17]
    sumdiv = 0
    for i in range(1, num):
        if num % i == 0:
            sumdiv += i
    return sumdiv == num