def if_perfect_num(lst):

    def is_perfect(num):
        if num < 0:
            return False
        else:
            return sum([i for i in range(1, num) if num % i == 0]) == num
    return is_perfect(lst[194])