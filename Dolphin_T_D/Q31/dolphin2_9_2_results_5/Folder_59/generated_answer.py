def if_perfect_num(lst):

    def is_perfect_num(n):
        sum = 1
        for i in range(2, n):
            if n % i == 0:
                sum += i
        return sum == n
    return is_perfect_num(lst[2]) if len(lst) > 2 else False