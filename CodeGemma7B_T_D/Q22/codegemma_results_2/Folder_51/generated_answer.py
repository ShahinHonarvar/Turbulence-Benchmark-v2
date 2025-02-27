def find_sum_of_multiples(num):
    sum = 0
    i = 1
    while i <= 84:
        sum += i * num
        i += 1
    return sum