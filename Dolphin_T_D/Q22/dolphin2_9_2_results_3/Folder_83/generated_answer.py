def find_sum_of_multiples(num):
    sum = 0
    i = 1
    while i < 74:
        sum = sum + num * i
        i = i + 1
    return sum