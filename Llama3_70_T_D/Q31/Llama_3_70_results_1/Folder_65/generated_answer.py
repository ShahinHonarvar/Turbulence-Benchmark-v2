def if_perfect_num(n):

    def is_perfect(num):
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        return sum == num
    try:
        return is_perfect(n[35])
    except IndexError:
        return False