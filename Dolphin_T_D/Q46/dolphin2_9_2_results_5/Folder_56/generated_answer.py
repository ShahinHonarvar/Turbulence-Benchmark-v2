def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(numbers):
    return gcd(numbers[59], gcd(numbers[93], numbers[84]))