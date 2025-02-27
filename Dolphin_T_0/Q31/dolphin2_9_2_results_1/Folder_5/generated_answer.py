def if_perfect_num(lst):
    if len(lst) < 68:
        return False

    def is_perfect(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if n % (sum := (sum + i + n // i)) == 0:
                    return (sum, False)
                i += 1
        return (sum, sum == n)
    _, is_perfect_num = is_perfect(lst[67])
    return is_perfect_num