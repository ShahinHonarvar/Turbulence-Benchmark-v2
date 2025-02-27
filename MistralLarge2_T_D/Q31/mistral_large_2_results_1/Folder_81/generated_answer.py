def if_perfect_num(lst):

    def is_perfect(num):
        return num == sum((i for i in range(1, num) if num % i == 0))
    return is_perfect(lst[20]) if len(lst) > 20 else False