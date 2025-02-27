def find_divisors_in_range(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    result = [i for i in divisors if 50 <= i <= 81]
    return result