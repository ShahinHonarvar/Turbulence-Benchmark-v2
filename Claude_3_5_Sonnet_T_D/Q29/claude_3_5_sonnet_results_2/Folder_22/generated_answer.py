def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 68 and isinstance(numbers[24], int) and isinstance(numbers[68], int):
        return gcd(abs(numbers[24]), abs(numbers[68]))
    else:
        return None