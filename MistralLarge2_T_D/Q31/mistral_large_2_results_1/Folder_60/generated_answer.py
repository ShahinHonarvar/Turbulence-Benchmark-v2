def if_perfect_num(lst):

    def is_perfect(num):
        sum_divisors = sum((i for i in range(1, num) if num % i == 0))
        return sum_divisors == num
    if len(lst) > 88:
        return is_perfect(lst[88])
    return False