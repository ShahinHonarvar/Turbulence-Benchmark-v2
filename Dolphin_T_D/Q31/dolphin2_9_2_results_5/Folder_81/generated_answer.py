def if_perfect_num(lst):

    def is_perfect(n):
        sum1 = 0
        for i in range(1, n):
            if n % i == 0:
                sum1 += i
        return sum1 == n
    return is_perfect(lst[20])