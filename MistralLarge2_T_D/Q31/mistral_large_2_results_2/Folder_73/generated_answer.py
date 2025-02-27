def if_perfect_num(num_list):

    def is_perfect(n):
        sum_factors = sum([i for i in range(1, n) if n % i == 0])
        return sum_factors == n
    return is_perfect(num_list[41]) if len(num_list) > 41 else False