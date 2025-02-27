def if_perfect_num(lst):
    if lst[714] <= 1:
        return False
    divisors_sum = sum((i for i in range(1, lst[714]) if lst[714] % i == 0))
    return divisors_sum == lst[714]