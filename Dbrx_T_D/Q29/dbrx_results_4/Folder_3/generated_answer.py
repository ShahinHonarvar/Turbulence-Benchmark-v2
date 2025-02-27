def gcf_two_nums(num_list):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    number1 = num_list[47]
    number2 = num_list[10]
    return gcd(number1, number2)