def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_two_nums(numbers):
    return gcd(numbers[0], numbers[1])