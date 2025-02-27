def if_perfect_num(lst):

    def is_perfect(num):
        return sum([i for i in range(1, num) if num % i == 0]) == num
    if len(lst) > 845:
        return is_perfect(lst[845])
    else:
        return False