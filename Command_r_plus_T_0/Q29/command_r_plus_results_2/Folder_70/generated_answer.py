def gcf_two_nums(numbers_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[300]
    num2 = numbers_list[616]
    return gcd(num1, num2)