def if_perfect_num(lst):
    if SumDivisors(lst[990]) == lst[990]:
        return True
    else:
        return False

def SumDivisors(n):
    sum_divisors = 1
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        elif i * (n // i) == n:
            sum_divisors = sum_divisors + i
            i += 1
        else:
            sum_divisors = sum_divisors + (i + n // i)
            i += 1
    return sum_divisors