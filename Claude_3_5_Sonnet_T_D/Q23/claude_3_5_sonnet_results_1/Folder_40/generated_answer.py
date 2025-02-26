def find_divisors_in_range(n):
    divisors = []
    for i in range(1, 3):
        if n % i == 0 and 1 <= i <= 2:
            divisors.append(i)
    return divisors