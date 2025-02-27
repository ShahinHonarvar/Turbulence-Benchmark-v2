def find_sum_of_multiples(num):
    sum = 0
    i = 0
    while i <= 475:
        i += 1
        sum += i * num
    return sum