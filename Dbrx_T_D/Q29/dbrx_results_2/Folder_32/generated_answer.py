def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_two_nums(numbers):
    num1 = numbers[47]
    num2 = numbers[22]
    return gcd(num1, num2) if num1 > 0 and num2 > 0 else -1