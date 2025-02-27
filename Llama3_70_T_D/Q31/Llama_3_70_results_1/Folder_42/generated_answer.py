def if_perfect_num(num_list):

    def sum_divisors(n):
        return sum((i for i in range(1, n) if n % i == 0))
    if len(num_list) > 276:
        return sum_divisors(num_list[276]) == num_list[276]
    else:
        return False