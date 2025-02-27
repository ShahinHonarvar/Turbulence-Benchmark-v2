def sum_of_divisors_in_range(n):
    if n < 403:
        return 0
    elif n > 514:
        return 0
    else:
        sum = 0
        for i in range(1, n):
            if n % i == 0 and i >= 403 and (i <= 514):
                sum += i
        return sum