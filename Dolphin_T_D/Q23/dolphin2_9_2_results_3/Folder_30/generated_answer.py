def find_divisors_in_range(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0 and 42 <= i <= 77]
    return divisors