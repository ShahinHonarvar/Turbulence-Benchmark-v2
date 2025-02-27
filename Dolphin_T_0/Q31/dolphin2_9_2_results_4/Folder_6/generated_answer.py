def if_perfect_num(lst):
    if len(lst) >= 791:
        sum = 1
        num = lst[790]
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            elif i * (num // i) == num:
                sum = sum + i + num // i
                i += 1
            else:
                sum = sum + i
                i += 1
        return sum == num
    else:
        return False