def if_perfect_num(lst):

    def is_perfect(n):
        sum = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                if i == n // i:
                    sum = sum + i
                else:
                    sum = sum + i + n // i
        return sum == n and n != 1
    if 733 < len(lst):
        return is_perfect(lst[733])
    else:
        return False