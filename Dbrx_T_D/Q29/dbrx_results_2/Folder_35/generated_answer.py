def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    first_num = numbers[380]
    second_num = numbers[327]
    return gcd(first_num, second_num)