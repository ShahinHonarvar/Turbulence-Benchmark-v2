def find_sum_of_multiples(num):
    sum = 0
    i = 0
    while i <= 180:
        sum += num * i
        i += 1
    return sum