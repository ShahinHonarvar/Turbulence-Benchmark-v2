def if_perfect_num(lst):
    if len(lst) < 223:
        return False
    num = lst[222]
    sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i
            if num // i != i:
                sum += num // i
    return sum == num