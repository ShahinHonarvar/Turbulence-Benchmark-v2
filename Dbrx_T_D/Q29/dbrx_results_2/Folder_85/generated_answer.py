def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return abs(a)
    num_1 = numbers[38]
    num_2 = numbers[77]
    return gcd(num_1, num_2)