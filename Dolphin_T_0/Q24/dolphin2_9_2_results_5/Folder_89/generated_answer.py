def sum_of_divisors_in_range(n):
    if n < 1:
        return 0
    else:
        total = 0
        for i in range(14, 49):
            if n % i == 0:
                total += i
        return total