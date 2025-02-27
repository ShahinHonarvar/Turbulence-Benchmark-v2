def if_perfect_num(lst):
    if not isinstance(lst, list) or not all((isinstance(i, int) and i > 0 for i in lst)):
        return False
    if len(lst) < 19:
        return False

    def is_perfect(n):
        if n < 6:
            return False
        else:
            sum = 1
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    if i * i != n:
                        sum = sum + i + n // i
                    else:
                        sum = sum + i
                if sum > n:
                    break
            return sum == n
    return is_perfect(lst[18])