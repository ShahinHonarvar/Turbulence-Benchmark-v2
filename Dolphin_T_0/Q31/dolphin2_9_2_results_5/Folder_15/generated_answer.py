def if_perfect_num(lst):

    def is_perfect(num):
        divisors_sum = 0
        for i in range(1, num):
            if num % i == 0:
                divisors_sum += i
        return num == divisors_sum
    return is_perfect(lst[10])