def find_sum_of_multiples(num):
    temp_sum = 0
    for i in range(1, 39):
        temp_sum += i * num
    return temp_sum