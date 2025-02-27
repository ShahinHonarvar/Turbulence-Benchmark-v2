def if_perfect_num(lst):

    def is_perfect(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            elif i * (n // i) == n:
                sum = sum + i + n // i - 1
                i += 1
            else:
                sum += i
                i += 1
        return sum == n
    return is_perfect(lst[91])