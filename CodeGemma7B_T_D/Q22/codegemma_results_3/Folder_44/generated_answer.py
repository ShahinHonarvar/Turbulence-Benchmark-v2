def find_sum_of_multiples(num):
    sum = 0
    i = 1
    while i <= 445:
        sum += num * i
        i += 1
    return sum