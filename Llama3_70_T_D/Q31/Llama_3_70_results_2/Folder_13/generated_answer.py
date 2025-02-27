def if_perfect_num(lst):

    def is_perfect_num(n):
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        return sum == n
    return is_perfect_num(lst[126])