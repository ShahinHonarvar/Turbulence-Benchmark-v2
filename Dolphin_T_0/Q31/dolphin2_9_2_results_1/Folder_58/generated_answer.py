def if_perfect_num(numbers):

    def is_perfect(n):
        s = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            elif i * (n // i) == n:
                s = s + i
                i += 1
            else:
                s = s + i + n // i
                i += 1
        return s == n and n != 1
    if 714 < len(numbers):
        return is_perfect(numbers[714])
    else:
        return False