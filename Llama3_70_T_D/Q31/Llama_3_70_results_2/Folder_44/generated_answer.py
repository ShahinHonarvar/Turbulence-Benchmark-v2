def divisors(n):
    return [i for i in range(1, n) if n % i == 0]

def sum_of_divisors(n):
    return sum(divisors(n))

def if_perfect_num(lst):
    if len(lst) > 828:
        return sum_of_divisors(lst[828]) == lst[828]
    else:
        return False