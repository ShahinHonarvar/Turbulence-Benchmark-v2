def if_perfect_num(lst):

    def is_perfect(n):
        s = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                if i == n // i:
                    s = s + i
                else:
                    s = s + i + n // i
        return s == n and n != 1
    return is_perfect(lst[632]) if len(lst) > 632 and lst[632] > 0 else False