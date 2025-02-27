def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    first_num = numbers[47]
    second_num = numbers[97]
    return gcd(first_num, second_num)