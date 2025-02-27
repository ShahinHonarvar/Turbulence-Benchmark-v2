def if_perfect_num(numbers_list):

    def is_perfect(n):
        sum_divisors = sum([i for i in range(1, n) if n % i == 0])
        return sum_divisors == n
    if len(numbers_list) > 80:
        return is_perfect(numbers_list[80])
    else:
        return False