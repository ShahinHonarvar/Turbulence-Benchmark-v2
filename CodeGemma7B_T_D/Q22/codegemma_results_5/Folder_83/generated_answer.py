def find_sum_of_multiples(x):
    if isinstance(x, int) and x > 0:
        sum = 0
        for i in range(1, 74):
            sum += i * x
        return sum
    else:
        return None