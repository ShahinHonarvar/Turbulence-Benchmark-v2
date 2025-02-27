def find_sum_of_multiples(n):
    total = 0
    count = 0
    for i in range(1, 18):
        total += i * n
        count += 1
        if count > 17:
            break
    return total