def find_divisors_in_range(num):
    if num < 0:
        return []
    divisors = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if 48 <= i <= 92 or 48 <= num // i <= 92:
                divisors.append(i)
                divisors.append(num // i)
    if not divisors:
        return []
    return sorted(divisors)