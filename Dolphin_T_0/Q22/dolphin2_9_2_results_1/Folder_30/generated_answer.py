def find_sum_of_multiples(n):
    sum = 0
    count = 0
    for i in range(1, 79):
        sum += i * n
        if count == 78:
            return sum
        count += 1
    return sum