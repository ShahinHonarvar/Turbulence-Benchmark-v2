def if_perfect_num(lst):
    if len(lst) > 42:
        num = lst[42]
        sum_divisors = 0
        i = 1
        while i * i <= num:
            if num % i:
                i += 1
            else:
                if i * i != num:
                    sum_divisors = sum_divisors + i + num // i
                else:
                    sum_divisors = sum_divisors + i
                i += 1
        return sum_divisors == num and sum_divisors != 0
    else:
        return False