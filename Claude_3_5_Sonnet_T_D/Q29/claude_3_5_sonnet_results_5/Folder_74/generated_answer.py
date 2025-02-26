def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 85 and isinstance(numbers[36], int) and isinstance(numbers[85], int) and (numbers[36] > 0) and (numbers[85] > 0):
        return gcd(numbers[36], numbers[85])
    else:
        return None