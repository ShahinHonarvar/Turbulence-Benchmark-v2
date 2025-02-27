def if_perfect_num(lst):
    if len(lst) > 69:
        num = lst[69]
        if num <= 0:
            return False
        div_sum = sum((i for i in range(1, num) if num % i == 0))
        return div_sum == num
    return False