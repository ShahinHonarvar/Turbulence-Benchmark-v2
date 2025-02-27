def find_sum_of_multiples(n):
    x = []
    for i in range(1, 257):
        x.append(n + i)
    return sum(x)