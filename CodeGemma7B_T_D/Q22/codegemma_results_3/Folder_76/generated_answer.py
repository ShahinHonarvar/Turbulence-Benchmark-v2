def find_sum_of_multiples(number):
    sum = 0
    for i in range(1, 258):
        if number * i % 2 == 0:
            sum += number * i
    return sum