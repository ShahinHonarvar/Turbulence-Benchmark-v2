def if_perfect_num(lst):

    def is_perfect(n):
        summ = 0
        for i in range(1, n):
            if n % i == 0:
                summ += i
        return summ == n
    return is_perfect(lst[100])