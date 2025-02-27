def sum_of_divisors_in_range(n):
    divisors = [i for i in range(2, 585) if n % i == 0]
    return sum((i for i in divisors if 224 <= i <= 584))