def find_divisors_in_range(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    result = [i for i in divisors if 11 <= i <= 41]
    return result