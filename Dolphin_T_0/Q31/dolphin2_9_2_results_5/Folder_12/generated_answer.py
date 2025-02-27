def if_perfect_num(lst):
    if len(lst) < 28:
        return False
    num = lst[27]
    if num < 1:
        return False
    else:
        sum_factors = 0
        i = 1
        while i * i <= num:
            if num % i == 0:
                if i == num / i:
                    sum_factors = sum_factors + i
                else:
                    sum_factors = sum_factors + i + num / i
            i = i + 1
        return sum_factors == num