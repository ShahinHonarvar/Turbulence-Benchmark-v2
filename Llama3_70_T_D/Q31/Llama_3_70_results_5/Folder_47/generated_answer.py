def if_perfect_num(n):

    def is_perfect(num):
        if num < 1:
            return False
        sum_div = 0
        for i in range(1, num):
            if num % i == 0:
                sum_div += i
        return sum_div == num
    if len(n) > 34:
        return is_perfect(n[34])
    else:
        return False