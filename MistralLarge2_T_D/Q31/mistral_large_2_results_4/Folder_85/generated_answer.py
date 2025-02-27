def if_perfect_num(num_list):

    def is_perfect(n):
        sum_divisors = sum((i for i in range(1, n) if n % i == 0))
        return sum_divisors == n
    return is_perfect(num_list[23]) if len(num_list) > 23 else False