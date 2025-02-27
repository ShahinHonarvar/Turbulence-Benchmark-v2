def if_perfect_num(lst):

    def is_perfect(n):
        if n < 1:
            return False
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if i * (n // i) == n:
                    sum_i = i
                    sum_n_i = n // i
                else:
                    sum_i = i
                    sum_n_i = i + n // i
                sum = sum + sum_i + sum_n_i
                i += 1
        return sum == n and n != 1
    if len(lst) > 90:
        return is_perfect(lst[90])
    else:
        return False