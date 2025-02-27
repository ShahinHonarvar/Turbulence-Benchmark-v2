def if_perfect_num(lst):
    if len(lst) <= 48 or lst[48] <= 0:
        return False
    num = lst[48]
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num