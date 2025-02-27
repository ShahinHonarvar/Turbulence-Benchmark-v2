def find_sum_of_multiples(multiple):
    sum = 0
    for i in range(223):
        sum += multiple * i
    return sum