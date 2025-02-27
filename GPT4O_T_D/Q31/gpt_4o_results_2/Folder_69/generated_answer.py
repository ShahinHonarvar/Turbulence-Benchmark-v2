def if_perfect_num(lst):
    if len(lst) <= 459:
        return False
    num = lst[459]
    if num < 2:
        return False
    total = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            total += i
            if i != num // i:
                total += num // i
    return total == num