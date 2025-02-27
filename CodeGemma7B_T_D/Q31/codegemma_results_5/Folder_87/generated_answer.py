def if_perfect_num(lst):
    num = lst[96]
    sum_of_div = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_of_div += i + num // i
    if sum_of_div == num:
        return True
    return False