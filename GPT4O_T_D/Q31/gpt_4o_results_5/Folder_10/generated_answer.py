def if_perfect_num(lst):
    if len(lst) <= 54:
        return False
    num = lst[54]
    if num <= 0:
        return False
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum == num