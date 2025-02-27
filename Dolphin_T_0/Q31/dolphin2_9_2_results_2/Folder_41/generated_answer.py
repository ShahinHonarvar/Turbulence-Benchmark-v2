def if_perfect_num(lst):

    def is_perfect_number(n):
        total = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if n % (i * i) == i:
                    total = total + i
                else:
                    total = total + (i + n // i)
                i += 1
        return total == n and n != 1
    return is_perfect_number(lst[84])