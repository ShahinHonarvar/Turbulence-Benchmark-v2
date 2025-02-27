def find_sum_of_multiples(num):
    multiples_sum = 0
    for i in range(1, 34):
        multiples_sum += num * i
    return multiples_sum