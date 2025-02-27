def if_perfect_num(num_list):

    def is_perfect(n):
        sum_of_divisors = sum((i for i in range(1, n) if n % i == 0))
        return sum_of_divisors == n
    if len(num_list) > 47:
        return is_perfect(num_list[47])
    return False