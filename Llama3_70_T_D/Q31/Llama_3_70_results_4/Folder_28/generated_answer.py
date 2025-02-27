def if_perfect_num(num_list):

    def is_perfect(n):
        sum = 0
        for x in range(1, n):
            if n % x == 0:
                sum += x
        return sum == n
    return is_perfect(num_list[37])