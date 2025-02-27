def if_perfect_num(num_list):

    def is_perfect(n):
        if n < 1:
            return False
        sum_divisors = sum((i for i in range(1, n) if n % i == 0))
        return sum_divisors == n
    if len(num_list) > 8:
        return is_perfect(num_list[8])
    else:
        return False