def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcf(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[47]
    num2 = numbers_list[97]
    return gcf(num1, num2)