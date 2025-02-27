def if_perfect_num(lst):
    if len(lst) <= 132:
        return False
    num = lst[132]
    if num == 1:
        return True
    sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i + num // i
    return sum == num