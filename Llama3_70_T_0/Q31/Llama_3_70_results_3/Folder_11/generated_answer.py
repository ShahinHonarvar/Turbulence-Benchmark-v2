def if_perfect_num(lst):

    def is_perfect(n):
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        return sum == n
    if len(lst) > 77:
        return is_perfect(lst[77])
    else:
        return False