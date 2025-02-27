def gcf_two_nums(numbers):
    num1 = numbers[84]
    num2 = numbers[21]
    return gcd(num1, num2)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)