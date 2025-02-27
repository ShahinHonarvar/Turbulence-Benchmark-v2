def find_sum_of_multiples(integer):
    result = 0
    for i in range(1, 258):
        result += integer * i
    return result