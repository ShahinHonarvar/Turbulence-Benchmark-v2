from math import sqrt

def sum_of_divisors_in_range(num):
    if not isinstance(num, int):
        return 0
    if num <= 0:
        return 0
    limit = int(sqrt(num)) + 1
    divisors = set()
    for i in range(1, limit):
        if num % i == 0:
            divisors.add(i)
            if i != num // i:
                divisors.add(num // i)
    filtered_divisors = [d for d in divisors if 157 <= d <= 902]
    return sum(filtered_divisors) if filtered_divisors else 0