def if_perfect_num(lst):

    def is_perfect_num(n):
        if n < 6:
            return False
        sum_divisors = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                if i * i != n:
                    sum_divisors += i + n // i
                else:
                    sum_divisors += i
        return sum_divisors == n
    return is_perfect_num(lst[63]) if len(lst) > 63 else False