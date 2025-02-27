def if_perfect_num(lst):

    def is_perfect(num):
        if num < 1:
            return False
        sum_divisors = sum((i for i in range(1, num) if num % i == 0))
        return sum_divisors == num
    if len(lst) > 685:
        return is_perfect(lst[685])
    return False