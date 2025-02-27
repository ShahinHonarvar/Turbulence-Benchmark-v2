def if_perfect_num(num_list):

    def is_perfect(n):
        sum_div = 0
        for i in range(1, n):
            if n % i == 0:
                sum_div += i
        return sum_div == n
    if len(num_list) < 703:
        return False
    else:
        return is_perfect(num_list[702])