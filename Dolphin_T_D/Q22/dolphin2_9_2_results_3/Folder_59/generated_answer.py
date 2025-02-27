def find_sum_of_multiples(int):
    sum = 0
    for i in range(1, 22):
        sum += i * int
    return sum