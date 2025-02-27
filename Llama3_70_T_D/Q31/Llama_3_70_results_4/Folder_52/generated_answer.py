def if_perfect_num(lst):

    def is_perfect_num(n):
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n
    if len(lst) <= 478:
        return False
    return is_perfect_num(lst[478])