def sum_divisors(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum

def if_perfect_num(lst):
    if len(lst) > 849:
        return lst[849] == sum_divisors(lst[849])
    return False