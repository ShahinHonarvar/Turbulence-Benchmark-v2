def if_perfect_num(lst):
    if len(lst) > 453:
        n = lst[453]
        divisors_sum = sum((i for i in range(1, n) if n % i == 0))
        return divisors_sum == n
    return False