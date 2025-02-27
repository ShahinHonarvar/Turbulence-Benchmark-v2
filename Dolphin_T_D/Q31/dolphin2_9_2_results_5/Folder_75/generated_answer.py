def if_perfect_num(lst):

    def is_perfect(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if i * (n // i) == n:
                    sum = sum + i + n // i
                else:
                    sum = sum + i
                i += 1
        if sum == n:
            return True
        else:
            return False
    if len(lst) > 80:
        return is_perfect(lst[80])
    else:
        return False