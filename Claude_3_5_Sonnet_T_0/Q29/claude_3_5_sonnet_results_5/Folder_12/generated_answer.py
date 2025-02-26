def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[56]
    num2 = numbers[54]
    return calculate_gcf(num1, num2)