def if_perfect_num(lst):

    def is_perfect(num):
        s = 0
        for i in range(1, num):
            if num % i == 0:
                s += i
        return num == s
    return is_perfect(lst[85])