def if_perfect_num(lst):

    def is_perfect(n):
        perfect_sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            elif n % (i * i) == 0:
                perfect_sum += i
                i += 1
            else:
                perfect_sum += i
                perfect_sum += n // i
                i += 1
        return perfect_sum == n and n != 1
    if len(lst) > 132 and is_perfect(lst[132]):
        return True
    else:
        return False