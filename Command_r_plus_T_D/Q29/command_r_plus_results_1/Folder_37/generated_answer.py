def gcf_two_nums(numbers_list: list[int]) -> int:
    num1 = numbers_list[29]
    num2 = numbers_list[74]
    gcf = 1
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf