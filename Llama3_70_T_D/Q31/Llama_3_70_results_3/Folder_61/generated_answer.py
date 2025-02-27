def if_perfect_num(lst):

    def is_perfect(n):
        if n < 1:
            return False
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        return sum == n
    try:
        return is_perfect(lst[8])
    except IndexError:
        return False