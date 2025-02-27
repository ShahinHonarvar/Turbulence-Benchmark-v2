def if_perfect_num(lst):

    def is_perfect(num):
        sum_of_divisors = sum((i for i in range(1, num) if num % i == 0))
        return sum_of_divisors == num
    return is_perfect(lst[19]) if len(lst) > 19 else False