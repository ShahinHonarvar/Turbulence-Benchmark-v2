def is_perfect_number(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def if_perfect_num(lst):
    if len(lst) > 702:
        return is_perfect_number(lst[702])
    return False