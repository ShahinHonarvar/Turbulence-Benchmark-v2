def if_perfect_num(lst):

    def is_perfect(n):
        if n < 0:
            return False
        perfect_sum = 0
        for i in range(1, n):
            if n % i == 0:
                perfect_sum += i
        return perfect_sum == n
    return is_perfect(lst[95])