def if_perfect_num(lst):
    if len(lst) > 733:
        num = lst[733]
        div_sum = 0
        for i in range(1, num):
            if num % i == 0:
                div_sum += i
        if div_sum == num:
            return True
        else:
            return False
    else:
        return False