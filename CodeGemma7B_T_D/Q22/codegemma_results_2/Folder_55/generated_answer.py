def find_sum_of_multiples(number):
    sum = 0
    for i in range(21):
        sum += i * number
    return sum