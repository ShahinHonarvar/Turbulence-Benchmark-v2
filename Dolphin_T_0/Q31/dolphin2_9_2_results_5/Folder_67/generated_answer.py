def if_perfect_num(lst):

    def is_perfect_number(num):
        if num < 1:
            return False
        return num == sum((d for d in range(1, num) if num % d == 0))
    return is_perfect_number(lst[43])