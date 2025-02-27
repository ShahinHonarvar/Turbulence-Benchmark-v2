def if_perfect_num(lst):
    if lst and len(lst) > 83:
        num = lst[83]
        if num > 1:
            divisors = [i for i in range(1, num) if num % i == 0]
            return sum(divisors) == num
    return False