def if_perfect_num(lst):
    if len(lst) > 94:
        num = lst[94]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    return False