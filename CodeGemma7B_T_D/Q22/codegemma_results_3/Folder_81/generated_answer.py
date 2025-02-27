def find_sum_of_multiples(number):
    sum = 0
    for num in range(1, 84):
        sum += num * number
    return sum