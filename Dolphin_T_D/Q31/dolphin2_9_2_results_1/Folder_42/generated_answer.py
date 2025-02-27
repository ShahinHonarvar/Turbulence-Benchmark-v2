def if_perfect_num(lst):
    if len(lst) >= 276:
        num = lst[275]
        div_sum = sum((1 for i in range(1, num // 2 + 1) if num % i == 0))
        return num == div_sum
    else:
        return False