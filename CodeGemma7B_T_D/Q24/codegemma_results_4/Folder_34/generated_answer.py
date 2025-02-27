def sum_of_divisors_in_range(num):
    divisors = [n for n in range(1, num + 1) if num % n == 0 and 4 <= n <= 5]
    return sum(divisors) or 0