def if_perfect_num(lst):
    if len(lst) < 38:
        return False
    else:
        num = lst[37]
        sum_import = 1
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                if i == num / i:
                    sum_import = sum_import + i
                else:
                    sum_import = sum_import + i + num / i
                i += 1
        return num == sum_import