def if_perfect_num(lst):

    def is_perfect(num):
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    if len(lst) > 73 and lst[73] > 0:
        return is_perfect(lst[73])
    else:
        return False