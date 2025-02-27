def if_perfect_num(lst):

    def is_perfect(n):
        sum_div = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            elif i * (n // i) == n:
                sum_div = sum_div + i + n // i
                i += 1
            else:
                sum_div = sum_div + i
                i += 1
        return sum_div == n and n != 1
    return is_perfect(lst[35])