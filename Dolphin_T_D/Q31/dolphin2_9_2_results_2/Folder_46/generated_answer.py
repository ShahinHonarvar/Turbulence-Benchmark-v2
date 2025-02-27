def if_perfect_num(lst):

    def is_perfect_number(n):
        sum = 1
        for i in range(2, n):
            if n % i == 0:
                sum += i
        return sum == n
    if 453 < len(lst):
        return is_perfect_number(lst[453])
    else:
        return False