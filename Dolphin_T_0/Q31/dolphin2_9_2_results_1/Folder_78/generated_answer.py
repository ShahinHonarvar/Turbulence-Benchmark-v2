def sum_divisors(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum

def if_perfect_num(lst):
    if lst[91] == sum_divisors(lst[91]):
        return True
    else:
        return False