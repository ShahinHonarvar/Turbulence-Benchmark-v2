def gcf_two_nums(numbers_list: list[int]) -> int:
    num1 = numbers_list[27]
    num2 = numbers_list[34]
    smaller_num = min(num1, num2)
    while smaller_num > 0:
        if num1 % smaller_num == 0 and num2 % smaller_num == 0:
            return smaller_num
        smaller_num -= 1