def find_sum_of_multiples(n):
    count = 0
    sum_of_multiples = 0
    i = 1
    while count < 77:
        if i % n == 0:
            sum_of_multiples += i
            count += 1
        i += 1
    return sum_of_multiples