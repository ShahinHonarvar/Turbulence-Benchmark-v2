def if_perfect_num(lst):
    if len(lst) <= 29:
        return False
    num = lst[29]
    divisors = [i for i in range(1, num // 2 + 1) if num % i == 0]
    return sum(divisors) == num