def gcf_two_nums(numbers_list: list[int]) -> int:
    num1 = numbers_list[96]
    num2 = numbers_list[57]
    gcf = 1
    for i in range(2, min(num1, num2) + 1):
        while num1 % i == 0 and num2 % i == 0:
            num1 //= i
            num2 //= i
            gcf *= i
    return gcf