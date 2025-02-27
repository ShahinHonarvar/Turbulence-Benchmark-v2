def if_perfect_num(lst):

    def is_perfect(n):
        if n == 0:
            return False
        else:
            sum_div = 1
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    sum_div += i
                    if i != n // i:
                        sum_div += n // i
            return sum_div == n
    return is_perfect(lst[478])