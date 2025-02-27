def divisors(n):
    return [i for i in range(1, n) if n % i == 0]

def if_perfect_num(lst):
    if len(lst) <= 57:
        return False
    num = lst[57]
    return sum(divisors(num)) == num