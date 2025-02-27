def if_perfect_num(lst):
    if len(lst) < 79:
        return False
    else:
        num = lst[78]
        if num == 0:
            return False
        else:
            div_sum = 1
            i = 2
            while i * i <= num:
                if num % i:
                    i += 1
                else:
                    if i == num / i:
                        div_sum = div_sum + i
                    else:
                        div_sum = div_sum + i + num // i
                    i += 1
            return div_sum == num