def sum_of_divisors_in_range(num):
    result = 0
    for i in range(1, num + 1):
        if num % i == 0 and 6 <= i <= 7:
            result += i
    return result if result > 0 else 0