def if_perfect_num(lst):

    def is_perfect(n):
        if n < 1:
            return False
        else:
            s = 1
            i = 2
            while i * i <= n:
                if n % i:
                    i += 1
                else:
                    if i * (n // i) == n:
                        s = s + i + n // i
                    else:
                        s = s + i
                    i += 1
            return s == n
    if len(lst) < 35:
        return False
    else:
        return is_perfect(lst[34])