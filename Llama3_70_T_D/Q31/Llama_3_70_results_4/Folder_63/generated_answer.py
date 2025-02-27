def if_perfect_num(lst):

    def is_perfect(n):
        if n < 1:
            return False
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n
    return is_perfect(lst[57]) if len(lst) > 57 else False