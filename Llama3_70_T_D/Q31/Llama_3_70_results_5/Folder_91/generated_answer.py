def if_perfect_num(num_list):

    def is_perfect(n):
        if n < 1:
            return False
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        return sum == n
    return len(num_list) > 6 and is_perfect(num_list[6])