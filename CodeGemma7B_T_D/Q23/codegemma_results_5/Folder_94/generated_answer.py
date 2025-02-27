def find_divisors_in_range(num):
    div = [i for i in range(35, 38) if num % i == 0]
    if not div:
        return []
    return div