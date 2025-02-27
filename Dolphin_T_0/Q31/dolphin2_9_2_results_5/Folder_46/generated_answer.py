def if_perfect_num(lst):
    if len(lst) < 454:
        return False
    num = lst[453]
    sum = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            if i == num / i:
                sum += i
            else:
                sum += i
                sum += num / i
        i += 1
    return sum == num