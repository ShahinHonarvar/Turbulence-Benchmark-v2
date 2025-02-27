def find_divisors_in_range(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    result = []
    for divisor in divisors:
        if 84 <= divisor <= 86:
            result.append(divisor)
    return result