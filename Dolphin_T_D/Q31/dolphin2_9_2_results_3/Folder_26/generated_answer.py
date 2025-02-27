def if_perfect_num(lst):

    def is_perfect(num):
        sum_divisors = 1
        for i in range(2, num):
            if num % i == 0:
                sum_divisors += i
        return sum_divisors == num
    if 222 < len(lst):
        return is_perfect(lst[222])
    else:
        return False