def if_perfect_num(lst):

    def is_perfect(num):
        return num > 1 and sum((div for div in range(1, num) if num % div == 0)) == num
    return is_perfect(lst[16]) if len(lst) > 16 else False