def if_perfect_num(n):

    def is_perfect(num):
        return sum((i for i in range(1, num) if num % i == 0)) == num
    try:
        return is_perfect(n[23])
    except IndexError:
        return False