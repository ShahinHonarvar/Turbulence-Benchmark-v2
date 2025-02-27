def if_perfect_num(lst):
    if len(lst) < 22:
        return False
    num = lst[21]
    if num <= 0:
        return False
    else:
        sum = 1
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                if i * (num // i) == num:
                    sum = sum + i + num // i
                else:
                    sum = sum + i
                i += 1
        return sum == num