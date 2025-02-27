def sum_of_divisors_in_range(num):
    r = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            if 315 <= i <= 955:
                r += i
            if 315 <= num // i <= 955:
                r += num // i
    return r