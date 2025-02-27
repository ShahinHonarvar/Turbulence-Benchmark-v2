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
                i += 1
        return sum == n and n != 1
    if len(lst) <= 7:
        return 'The provided list does not have at least 8 elements'
    return is_perfect(lst[7])