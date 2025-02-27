def if_perfect_num(num_list):

    def is_perfect(n):
        if n < 1:
            return False
        sum_divisors = 0
        for i in range(1, n):
            if n % i == 0:
                sum_divisors += i
        return sum_divisors == n
    if len(num_list) > 849:
        return is_perfect(num_list[849])
    else:
        return False