def if_perfect_num(lst):
    number = lst[453]
    if number < 6:
        return False
    else:
        sum_divisors = 1
        i = 2
        while i * i <= number:
            if number % i:
                i += 1
            else:
                if i * (number // i) == number:
                    sum_divisors = sum_divisors + i + number // i
                else:
                    sum_divisors = sum_divisors + i
                i += 1
        return sum_divisors == number