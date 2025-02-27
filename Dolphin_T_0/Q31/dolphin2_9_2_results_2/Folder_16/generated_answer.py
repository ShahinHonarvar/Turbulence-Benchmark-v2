def if_perfect_num(lst):
    if len(lst) > 162:
        num = lst[162]
        sum_divisors = 0
        i = 1
        while i * i <= num:
            if num % i == 0:
                if i * i == num:
                    sum_divisors += i
                else:
                    sum_divisors += i + num // i
            i += 1
        return sum_divisors == num and num != 1
    return False