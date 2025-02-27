def gcf_two_nums(numbers):
    if len(numbers) >= 225 and len(numbers) >= 664:
        num1 = numbers[224]
        num2 = numbers[663]
        i = 1
        while i <= min(num1, num2):
            if num1 % i == 0 and num2 % i == 0:
                common_factor = i
            i += 1
        return common_factor