def if_perfect_num(num_list):

    def is_perfect(n):
        return sum((i for i in range(1, n) if n % i == 0)) == n
    return is_perfect(num_list[99])