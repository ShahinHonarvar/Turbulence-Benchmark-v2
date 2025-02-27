def if_perfect_num(lst):
    if lst and len(lst) > 94:
        num = lst[94]
        sum_of_divisors = sum((i for i in range(1, num) if num % i == 0))
        return sum_of_divisors == num
    return False