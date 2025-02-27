def find_sum_of_multiples(num):
    sum_mult = 0
    i = 1
    while i <= 25:
        sum_mult += i * num
        i += 1
    return sum_mult