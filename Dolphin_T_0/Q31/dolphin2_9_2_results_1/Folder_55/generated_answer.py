def if_perfect_num(lst):
    num = lst[21]
    if not isinstance(num, int) or num < 1:
        return False
    else:
        s = 1
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
                continue
            if i * (num // i) == num:
                s = s + i + num // i
            else:
                s = s + i
            i += 1
    return s == num