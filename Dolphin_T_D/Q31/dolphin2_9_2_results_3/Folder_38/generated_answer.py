def if_perfect_num(lst):
    if len(lst) > 38:
        num = lst[38]
        sum_of_factors = 0
        i = 1
        while i * i <= num:
            if num % i:
                i += 1
            else:
                if i * (num // i) == num:
                    sum_of_factors = sum_of_factors + i
                else:
                    sum_of_factors = sum_of_factors + (i + num // i)
                i += 1
        return sum_of_factors == num and num != 1
    else:
        return False