def if_perfect_num(lst):
    num = lst[0]
    perfect_sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            perfect_sum += i
            if i != num // i:
                perfect_sum += num // i
    return perfect_sum == num and len(lst) > 0