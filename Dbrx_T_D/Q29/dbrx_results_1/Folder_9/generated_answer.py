def gcf_two_nums(numbers):
    num1 = numbers[63]
    num2 = numbers[84]
    return gcd(num1, num2)

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a