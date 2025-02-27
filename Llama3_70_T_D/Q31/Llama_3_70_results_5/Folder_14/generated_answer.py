def if_perfect_num(n):

    def is_perfect(num):
        sum_divisors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_divisors += i
        return sum_divisors == num
    try:
        return is_perfect(n[17])
    except IndexError:
        return False