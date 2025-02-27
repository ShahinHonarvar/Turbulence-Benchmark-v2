def gcf_two_nums(numbers_list: list[int]) -> int:
    num1 = numbers_list[38]
    num2 = numbers_list[77]

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    return gcd(num1, num2)