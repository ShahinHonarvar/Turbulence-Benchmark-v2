def if_perfect_num(num_list):

    def is_perfect_num(n):
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n
    if len(num_list) > 29:
        return is_perfect_num(num_list[29])
    else:
        return False