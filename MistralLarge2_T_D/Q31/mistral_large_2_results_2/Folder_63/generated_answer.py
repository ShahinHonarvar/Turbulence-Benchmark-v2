def if_perfect_num(lst):

    def is_perfect(num):
        return num == sum((i for i in range(1, num) if num % i == 0))
    if len(lst) > 57:
        return is_perfect(lst[57])
    return False