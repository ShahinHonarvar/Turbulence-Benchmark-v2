def if_perfect_num(lst):

    def is_perfect_number(num):
        if num < 1:
            return False
        sum_divisors = 1
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                if i * (num // i) == num:
                    sum_divisors = sum_divisors + i + num // i
                else:
                    sum_divisors = sum_divisors + i
                i += 1
        return sum_divisors == num
    return is_perfect_number(lst[69]) if len(lst) > 69 else False