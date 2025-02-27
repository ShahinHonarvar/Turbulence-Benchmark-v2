def if_perfect_num(num_list):

    def is_perfect(n):
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        return sum == n
    if len(num_list) > 733 and num_list[733] > 0:
        return is_perfect(num_list[733])
    else:
        return False