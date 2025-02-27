def if_perfect_num(num_list):

    def sum_of_divisors(n):
        return sum((i for i in range(1, n) if n % i == 0))
    return sum_of_divisors(num_list[73]) == num_list[73]