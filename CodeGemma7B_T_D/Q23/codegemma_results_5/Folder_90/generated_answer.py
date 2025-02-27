def find_divisors_in_range(num):
    quad_root = int(451.5)
    for i in range(quad_root, num + 1):
        if num % i == 0 and num // i >= 451 and (num // i <= 973):
            yield i