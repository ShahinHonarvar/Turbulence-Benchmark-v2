def if_perfect_num(lst):

    def perfect_num(n):
        return sum((i for i in range(1, n) if n % i == 0)) == n
    if len(lst) > 59 and lst[59] > 0:
        return perfect_num(lst[59])
    else:
        return False