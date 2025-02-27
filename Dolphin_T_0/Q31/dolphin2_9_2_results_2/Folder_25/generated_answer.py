def if_perfect_num(lst):

    def is_perfect(n):
        sum = 1
        for i in range(2, n):
            if n % i == 0:
                sum += i
        return sum == n
    if len(lst) > 90:
        return is_perfect(lst[90])
    else:
        return False