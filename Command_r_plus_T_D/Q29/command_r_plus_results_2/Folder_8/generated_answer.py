def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[69]
    num2 = numbers_list[41]
    gcf = gcd(num1, num2)
    return gcf