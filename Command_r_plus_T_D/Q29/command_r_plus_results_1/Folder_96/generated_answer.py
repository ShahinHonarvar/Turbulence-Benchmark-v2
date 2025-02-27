def gcf_two_nums(numbers_list: list[int]) -> int:
    num1 = numbers_list[95]
    num2 = numbers_list[73]

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(num1, num2)