def find_divisors_in_range(number):
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    return [divisor for divisor in divisors if 50 <= divisor <= 84]