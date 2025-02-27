def find_sum_of_multiples(number):
    sum = 0
    for i in range(1, 117):
        sum += number * i
    return sum