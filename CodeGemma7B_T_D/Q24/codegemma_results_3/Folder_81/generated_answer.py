def sum_of_divisors_in_range(n):
    sum = 0
    for i in range(3, n):
        if n % i == 0 and i in range(3, 5):
            sum += i
    if sum == 0:
        return 0
    else:
        return sum