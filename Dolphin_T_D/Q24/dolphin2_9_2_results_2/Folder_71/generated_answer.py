def sum_of_divisors_in_range(n):
    result = 0
    for i in range(45, 73):
        if n % i == 0 and n / i == int(n / i):
            result += i
    return result