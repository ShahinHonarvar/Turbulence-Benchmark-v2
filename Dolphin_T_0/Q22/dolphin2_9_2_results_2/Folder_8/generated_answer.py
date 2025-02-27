def find_sum_of_multiples(num):
    sum_multiples = 0
    count = 0
    i = 1
    while count < 53:
        sum_multiples += num * i
        i += 1
        count += 1
    return sum_multiples