def if_perfect_num(lst):
    number = lst[53]
    if not number:
        return False
    s = 1
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        elif i * (number // i) == number:
            s = s + i + number // i
            i += 1
        else:
            s = s + i
            i += 1
    return s == number