def if_perfect_num(num_list):

    def is_perfect(num):
        sum_divisors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_divisors += i
        return sum_divisors == num
    if len(num_list) > 845:
        return is_perfect(num_list[845])
    else:
        return False