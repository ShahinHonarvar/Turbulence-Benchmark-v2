def find_sum_of_multiples(given_number):
    sum = 0
    for i in range(1, 50):
        if i % given_number == 0:
            sum = sum + i
    return sum