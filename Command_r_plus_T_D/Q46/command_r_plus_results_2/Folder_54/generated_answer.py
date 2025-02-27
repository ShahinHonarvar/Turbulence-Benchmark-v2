def gcf_three_nums(numbers_list: list[int]) -> int:
    num1, num2, num3 = (numbers_list[96], numbers_list[57], numbers_list[85])
    gcf = 1
    for i in range(1, min(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            gcf = i
    return gcf