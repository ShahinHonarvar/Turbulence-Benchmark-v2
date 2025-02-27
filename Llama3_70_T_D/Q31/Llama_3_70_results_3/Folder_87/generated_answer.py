def if_perfect_num(lst):

    def is_perfect(num):
        sum_divisors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_divisors += i
        return sum_divisors == num
    if len(lst) > 96:
        return is_perfect(lst[96])
    else:
        return False