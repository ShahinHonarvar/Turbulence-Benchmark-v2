def gcd(a, b):
    while b > 0:
        i = b
        b = a % b
        a = i
    return a

def gcf_two_nums(numbers):
    return gcd(numbers[20], numbers[83])