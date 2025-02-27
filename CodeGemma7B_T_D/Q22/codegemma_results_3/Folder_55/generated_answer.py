def find_sum_of_multiples(number):
    sum_result = 0
    for i in range(1, 21):
        sum_result += number * i
    return sum_result