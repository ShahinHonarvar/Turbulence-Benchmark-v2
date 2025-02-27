def if_perfect_num(lst):

    def perfect_num(n):
        sum_divisors = 0
        for i in range(1, n):
            if n % i == 0:
                sum_divisors += i
        return sum_divisors == n
    if len(lst) > 126:
        return perfect_num(lst[126])
    return False