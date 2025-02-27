def if_perfect_num(lst):
    perfect_num = lst[20]
    sum = 1
    for i in range(2, int(perfect_num ** 0.5) + 1):
        if perfect_num % i == 0:
            if i == perfect_num // i:
                sum = sum + i
            else:
                sum = sum + i + perfect_num // i
    return sum == perfect_num