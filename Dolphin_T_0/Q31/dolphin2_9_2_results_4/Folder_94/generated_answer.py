def if_perfect_num(lst):

    def is_perfect(n):
        if n < 1:
            return False
        else:
            sum = 1
            i = 2
            while i * i <= n:
                if n % i:
                    i += 1
                elif i * (n // i) == n:
                    sum = sum + i
                    i += 1
                else:
                    sum += i
                    sum += n // i
                    i += 1
            return sum == n and n != 1
    return is_perfect(lst[93])