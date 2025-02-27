def find_sum_of_multiples(n):
    result = []
    for i in range(1, 18):
        if n <= i:
            result.append(n * i)
    return sum(result)