def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)
    num_64 = numbers[64]
    num_28 = numbers[28]
    return lcm(num_64, num_28) if num_64 % num_28 == 0 else gcd(num_64, num_28)