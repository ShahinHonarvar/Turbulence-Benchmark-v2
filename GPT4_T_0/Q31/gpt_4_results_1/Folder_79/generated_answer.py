def if_perfect_num(lst):
    if len(lst) > 63:
        num = lst[63]
        divisors = [i for i in range(1, num) if num % i == 0]
        if sum(divisors) == num:
            return True
    return False