def if_perfect_num(lst):

    def is_perfect_number(n):
        if n == 1:
            return True
        else:
            div_sum = 1
            for i in range(2, n):
                if n % i == 0:
                    div_sum += i
            return div_sum == n
    return is_perfect_number(lst[24])