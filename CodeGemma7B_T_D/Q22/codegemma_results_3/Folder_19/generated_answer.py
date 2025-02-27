def find_sum_of_multiples(x):
    y = 0
    for i in range(1, 47):
        y += i * x
    return y