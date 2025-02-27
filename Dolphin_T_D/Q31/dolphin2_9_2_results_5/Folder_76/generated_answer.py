def if_perfect_num(int_list):

    def is_perfect(n):
        return n == sum(list(filter(lambda x: n % x == 0, range(1, n))))
    return is_perfect(int_list[537])