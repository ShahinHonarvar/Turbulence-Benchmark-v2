def find_divisors_in_range(n):
    div_range = list(range(7, 9))
    divisors = [div for div in div_range if n % div == 0]
    return divisors