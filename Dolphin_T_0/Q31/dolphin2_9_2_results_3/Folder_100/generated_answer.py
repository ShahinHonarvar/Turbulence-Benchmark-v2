def if_perfect_num(lst):

    def is_perfect(n):
        sum = 1
        root = int(n ** 0.5)
        for i in range(2, root + 1):
            if n % i == 0:
                if n // i == i:
                    sum += i
                else:
                    sum += i + n // i
        return sum == n
    return is_perfect(lst[99])