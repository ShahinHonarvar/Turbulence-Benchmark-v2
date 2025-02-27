def greatest_common_factor(num1, num2):
    """
    Calculate the greatest common factor of two numbers using the Euclidean algorithm.
    """
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1

def gcf_three_nums(numbers):
    """
    Calculate the greatest common factor of the elements at indices 36, 85 and 83.
    """
    num1 = numbers[36]
    num2 = numbers[85]
    num3 = numbers[83]
    gcf1 = greatest_common_factor(num1, num2)
    gcf2 = greatest_common_factor(gcf1, num3)
    return gcf2