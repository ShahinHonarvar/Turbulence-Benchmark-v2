def if_perfect_num(n):

    def is_perfect(num):
        if num < 1:
            return False
        sum_divisors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_divisors += i
        return sum_divisors == num
    if len(n) > 74:
        return is_perfect(n[74])
    else:
        return False