def if_perfect_num(lst):

    def is_perfect_number(n):
        if n < 0:
            return False
        sum = 1
        for i in range(2, n):
            if n % i == 0:
                sum += i
        return sum == n
    return is_perfect_number(lst[56])