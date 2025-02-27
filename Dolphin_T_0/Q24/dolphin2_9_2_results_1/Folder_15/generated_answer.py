def sum_of_divisors_in_range(n):
    result = 0
    for i in range(1, n + 1):
        if i > 9:
            break
        elif n % i == 0:
            result += i
    return result