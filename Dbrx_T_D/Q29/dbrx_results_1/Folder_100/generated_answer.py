import functools

def gcf_two_nums(numbers):
    num1 = numbers[96]
    num2 = numbers[32]
    if num1 < 0 or num2 < 0:
        raise ValueError('All numbers must be positive')
    if num1 < num2:
        num1, num2 = (num2, num1)
    if num2 == 0:
        return num1
    return gcd(num1, num2)

@functools.singledispatch
def gcd(a, b):
    raise TypeError('Arguments must be integers')

@gcd.register(int, int)
def _gcd(a, b):
    return a // gcd(a % b, b) * b