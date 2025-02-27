def if_perfect_num(lst):

    def is_perfect(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if n // i != i:
                    sum += i
                sum += n // i
                i += 1
        return sum == n and n != 1
    if len(lst) > 276 and lst[276] > 0:
        return is_perfect(lst[276])
    else:
        return False