from fractions import gcd

def apply_gcd(numbers):
    return numbers[0] if len(numbers) == 1 else gcd(numbers[0], numbers[1])

def gcf_three_nums(numbers):
    return apply_gcd([apply_gcd([numbers[876], numbers[203]]), numbers[100]])