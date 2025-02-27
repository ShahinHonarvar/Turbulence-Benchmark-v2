def find_sum_of_multiples(n):
    output = 0
    for i in range(1, 186):
        output += i * n
    return output