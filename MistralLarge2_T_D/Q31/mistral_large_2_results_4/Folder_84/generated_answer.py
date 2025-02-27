def if_perfect_num(num_list):

    def is_perfect(n):
        return n == sum((i for i in range(1, n) if n % i == 0))
    return is_perfect(num_list[685]) if len(num_list) > 685 else False