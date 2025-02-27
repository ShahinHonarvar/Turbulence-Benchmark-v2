def sum_of_divisors_in_range(num):
    sum_of_divisors = sum([div for div in range(1, num + 1) if num % div == 0 and 14 <= div <= 48])
    return sum_of_divisors