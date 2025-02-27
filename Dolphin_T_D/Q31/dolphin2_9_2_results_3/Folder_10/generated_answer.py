def if_perfect_num(lst):

    def is_perfect(n):
        if n < 6:
            return False
        else:
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
    if len(lst) > 54 and is_perfect(lst[54]):
        return True
    else:
        return False