def if_perfect_num(lst):

    def is_perfect(n):
        if n < 6:
            return False
        sum = 1
        i = 2
        while i * i <= n:
            if n % i == 0:
                if n // i == i:
                    sum = sum + i
                else:
                    sum = sum + i + n // i
            i += 1
        return sum == n
    return is_perfect(lst[91])