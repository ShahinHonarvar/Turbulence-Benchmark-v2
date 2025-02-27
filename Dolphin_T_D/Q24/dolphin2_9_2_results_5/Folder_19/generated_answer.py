def sum_of_divisors_in_range(n):
    divisors = [1]
    for i in range(2, n + 1):
        if n % i == 0:
            divisors.append(i)
    divisors_in_range = [d for d in divisors if d >= 1 and d <= 7]
    return sum(divisors_in_range)