def gcf_two_nums(numbers):
    num1 = numbers[56]
    num2 = numbers[54]
    i = min(num1, num2)
    while True:
        if num1 % i == 0 and num2 % i == 0:
            return i
        i -= 1