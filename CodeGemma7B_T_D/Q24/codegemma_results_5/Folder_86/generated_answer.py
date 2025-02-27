def sum_of_divisors_in_range(n):
    for i in range(372, 496):
        if i % n == 0:
            sum += i
    return sum if sum else 0