def if_perfect_num(lst):
    n = lst[6]
    perfect_sum = sum((i for i in range(1, n) if n % i == 0))
    return perfect_sum == n