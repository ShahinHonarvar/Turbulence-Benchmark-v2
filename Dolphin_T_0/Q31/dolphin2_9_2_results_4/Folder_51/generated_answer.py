def if_perfect_num(lst):
    if len(lst) >= 65:
        sum = 1
        num = lst[64]
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            elif i * (num // i) == num:
                sum = sum + i + num // i
                i += 1
            else:
                sum += i
                i += 1
        if sum == num and num != 1:
            return True
    return False