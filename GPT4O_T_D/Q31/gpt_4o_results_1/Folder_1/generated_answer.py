def if_perfect_num(lst):
    if len(lst) <= 85:
        return False
    num = lst[85]
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num