def if_perfect_num(lst):
    if len(lst) <= 985:
        return False
    num = lst[985]
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num