def sum_of_divisors_in_range(n):
    sum = 0
    for i in range(658, 868 + 1):
        if i % n == 0:
            sum += i
    return sum if sum else 0