def if_perfect_num(lst):

    def perfect_num(n):
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        return sum == n
    if len(lst) > 94:
        return perfect_num(lst[94])
    else:
        return False