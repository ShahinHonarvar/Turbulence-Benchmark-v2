def if_perfect_num(lst):

    def is_perfect(n):
        sum = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                if i == int(n / i):
                    sum = sum + i
                else:
                    sum = sum + i + n // i
        return sum == n and n != 1
    return is_perfect(lst[20])