def if_perfect_num(lst):
    perfect_num = lst[92]
    sum1 = 1
    for i in range(2, int(perfect_num ** 0.5) + 1):
        if perfect_num % i == 0:
            if perfect_num / i == i:
                sum1 = sum1 + i
            else:
                sum1 = sum1 + (i + perfect_num // i)
    return sum1 == perfect_num