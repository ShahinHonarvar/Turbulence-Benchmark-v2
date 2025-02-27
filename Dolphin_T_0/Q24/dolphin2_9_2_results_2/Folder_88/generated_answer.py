def sum_of_divisors_in_range(n):
    result = 0
    for i in range(1, n + 1):
        if i % n == 0 and 6 <= i <= 7:
            result += i
    return result if result != 0 else 'No such divisors exist in the specified range'