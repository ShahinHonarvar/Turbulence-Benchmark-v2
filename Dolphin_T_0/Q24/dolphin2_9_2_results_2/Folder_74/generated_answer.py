def sum_of_divisors_in_range(num):
    sum = 0
    for i in range(1, num + 1):
        if i > 74:
            break
        if num % i == 0 and i >= 40:
            sum += i
    return sum