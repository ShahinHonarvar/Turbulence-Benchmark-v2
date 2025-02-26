def if_perfect_num(num_list):

    def is_perfect(n):
        if n <= 1:
            return False
        divisor_sum = sum((i for i in range(1, n) if n % i == 0))
        return divisor_sum == n
    if len(num_list) <= 702:
        return False
    return is_perfect(num_list[702])