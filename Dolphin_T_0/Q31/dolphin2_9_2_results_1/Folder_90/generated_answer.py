def if_perfect_num(num_list):

    def is_perfect_number(n):
        sum_div = 0
        for i in range(1, n):
            if n % i == 0:
                sum_div += i
        return sum_div == n
    return is_perfect_number(num_list[263])