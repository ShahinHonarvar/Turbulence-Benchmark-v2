def if_perfect_num(lst):

    def perfect_num(n):
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n
    if len(lst) > 849:
        return perfect_num(lst[849])
    else:
        return False