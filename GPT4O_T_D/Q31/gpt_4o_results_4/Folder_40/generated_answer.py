def if_perfect_num(lst):
    if len(lst) > 7:
        num = lst[7]
        factors = [i for i in range(1, num) if num % i == 0]
        return sum(factors) == num
    return False