def if_perfect_num(lst):

    def is_perfect(n):
        summ = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            elif i * (n // i) == n:
                summ = summ + i + n // i
                i += 1
            else:
                summ = summ + i
                i += 1
        return summ == n and n != 1
    if len(lst) > 8 and lst[8] > 1:
        return is_perfect(lst[8])
    else:
        return False