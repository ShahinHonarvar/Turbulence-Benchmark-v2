def if_perfect_num(num_list):

    def is_perfect(n):
        return sum((i for i in range(1, n) if n % i == 0)) == n
    if len(num_list) > 537 and num_list[537] > 0:
        return is_perfect(num_list[537])
    else:
        return False