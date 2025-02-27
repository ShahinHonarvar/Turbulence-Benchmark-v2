def if_perfect_num(lst):
    if len(lst) < 35:
        return False
    num = lst[34]
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num