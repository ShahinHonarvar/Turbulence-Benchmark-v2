def if_perfect_num(num_list):
    num = num_list[73]
    sum_of_divisors = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            if i * (num // i) == num:
                sum_of_divisors = sum_of_divisors + i + num // i
            i += 1
    return sum_of_divisors == num and num != 1