def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(numbers[1], numbers[2]) if numbers[1] < numbers[2] else gcd(numbers[2], numbers[1])