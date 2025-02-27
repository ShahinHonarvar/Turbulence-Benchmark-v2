def if_perfect_num(lst):
    if len(lst) <= 69 or lst[69] <= 1:
        return False
    num = lst[69]
    divisors_sum = sum((i for i in range(1, num // 2 + 1) if num % i == 0))
    return divisors_sum == num