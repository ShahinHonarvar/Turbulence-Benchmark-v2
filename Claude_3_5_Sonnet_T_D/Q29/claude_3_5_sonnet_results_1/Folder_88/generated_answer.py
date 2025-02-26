def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 34 and all((isinstance(num, int) and num > 0 for num in numbers)):
        return gcd(numbers[27], numbers[34])
    else:
        return None