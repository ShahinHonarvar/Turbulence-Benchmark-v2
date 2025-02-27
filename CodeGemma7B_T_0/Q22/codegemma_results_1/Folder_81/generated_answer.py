def find_sum_of_multiples(num):
    sum = 0
    for i in range(1, 84):
        sum += i * num
    return sum