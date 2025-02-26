def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 94 or not all((isinstance(num, int) and num > 0 for num in numbers)):
        return None
    return gcd(numbers[78], numbers[93])