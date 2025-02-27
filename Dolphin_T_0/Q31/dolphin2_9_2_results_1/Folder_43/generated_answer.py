def if_perfect_num(lst):
    num = lst[29]
    if num == 0:
        return False
    else:
        sum = 1
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
        return sum == num