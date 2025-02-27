def sum_of_divisors_in_range(num):
    result = 0
    for i in range(3, 7):
        if num % i == 0:
            result += i
    return result if result != 0 else result + 1