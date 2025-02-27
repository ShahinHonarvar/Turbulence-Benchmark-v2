def if_perfect_num(lst):

    def perfect_number(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if n % (i * i) != i:
                    sum = sum + i + n / i
                else:
                    sum = sum + i
                i += 1
        return sum == n
    return perfect_number(lst[35]) if len(lst) > 35 else False