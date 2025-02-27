def sum_of_divisors_in_range(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    valid_divisors = [div for div in divisors if 11 <= div <= 56]
    return sum(valid_divisors) if valid_divisors else 0