def if_perfect_num(lst):
    if len(lst) < 73:
        return False
    else:
        num = lst[72]
        sum1 = 0
        i = 1
        while i * i <= num:
            if num % i:
                i += 1
            else:
                if i * (num // i) == num:
                    sum1 = i + num // i
                else:
                    sum1 = i
                i += 1
        return sum1 == num and num != 0