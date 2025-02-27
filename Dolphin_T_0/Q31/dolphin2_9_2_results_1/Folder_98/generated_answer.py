def if_perfect_num(lst):
    if len(lst) < 5:
        return False
    else:
        number = lst[4]
        sum_of_divisors = 1
        i = 2
        while i * i <= number:
            if number % i:
                i += 1
            else:
                if i * (number // i) == number:
                    sum_of_divisors = sum_of_divisors + i + number // i
                else:
                    sum_of_divisors = sum_of_divisors + i
                i += 1
        return sum_of_divisors == number and number != 1