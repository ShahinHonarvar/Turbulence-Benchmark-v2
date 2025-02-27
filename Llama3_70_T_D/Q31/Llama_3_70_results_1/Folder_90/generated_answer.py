def if_perfect_num(lst):

    def is_perfect(n):
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        return sum == n
    return lst[263] == 0 or is_perfect(lst[263])