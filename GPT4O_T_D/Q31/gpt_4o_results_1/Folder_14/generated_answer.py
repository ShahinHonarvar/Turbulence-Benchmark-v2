def if_perfect_num(lst):
    if len(lst) <= 17:
        return False
    num = lst[17]
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num