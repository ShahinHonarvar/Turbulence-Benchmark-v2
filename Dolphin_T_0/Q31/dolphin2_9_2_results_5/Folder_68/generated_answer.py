def if_perfect_num(lst):

    def is_perfect_number(n):
        sum_divisors = 0
        i = 1
        while i * i <= n:
            if n % i == 0:
                sum_divisors += i
                if i * i != n:
                    sum_divisors += n // i
            i += 1
        return sum_divisors == n and n != 0
    return is_perfect_number(lst[3])