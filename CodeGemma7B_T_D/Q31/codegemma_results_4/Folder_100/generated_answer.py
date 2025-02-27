def if_perfect_num(lst):
    return lst[98] == perfect_num(lst[98])

def perfect_num(n):
    sum = 0
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            sum += i
    return sum == n