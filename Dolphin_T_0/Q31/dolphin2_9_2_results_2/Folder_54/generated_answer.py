def if_perfect_num(lst):
    if len(lst) >= 52:

        def is_perfect(n):
            sum_factors = 1
            i = 2
            while i * i <= n:
                if n % i:
                    i += 1
                else:
                    if i * (n // i) == n:
                        sum_factors = sum_factors + i + n // i
                    else:
                        sum_factors = sum_factors + i
                    i += 1
            return sum_factors == n
        return is_perfect(lst[51])
    else:
        return False