def if_perfect_num(lst):
    if 'lst' in locals():
        num = lst[88]
        div_sum = 0
        for i in range(1, num):
            if num % i == 0:
                div_sum += i
        if div_sum == num:
            return True
    return False