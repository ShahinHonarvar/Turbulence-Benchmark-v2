def find_divisors_in_range(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0 and 5 <= i <= 7]
    return divisors if divisors else []