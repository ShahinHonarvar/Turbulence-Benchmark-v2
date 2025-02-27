def if_perfect_num(lst):
    if len(lst) > 16:
        num = lst[16]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    return False