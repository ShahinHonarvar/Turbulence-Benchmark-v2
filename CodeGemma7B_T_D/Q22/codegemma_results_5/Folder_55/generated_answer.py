def find_sum_of_multiples(number):
    sum = 0
    for i in range(1, 21):
        sum += number * i
    return sum