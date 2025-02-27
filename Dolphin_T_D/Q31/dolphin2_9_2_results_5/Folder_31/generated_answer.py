def if_perfect_num(lst):
    num = lst[66]
    sum = 1
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            sum += i
    return sum == num