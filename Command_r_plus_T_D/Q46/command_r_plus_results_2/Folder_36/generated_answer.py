def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    if not numbers_list:
        raise ValueError('Input list is empty')
    if any((num <= 0 for num in numbers_list)):
        raise ValueError('Input list must contain only positive integers')
    num1 = numbers_list[427]
    num2 = numbers_list[761]
    num3 = numbers_list[148]
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf