def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    first_num = numbers[145]
    second_num = numbers[183]
    third_num = numbers[770]
    first_gcd = gcd(first_num, second_num)
    final_gcd = gcd(first_gcd, third_num)
    return final_gcd