def gcf(a, b):
    while b != 0:
        a = a % b
        a, b = (b, a)
    return a

def gcf_three_nums(numbers):
    return gcf(numbers[56], gcf(numbers[88], numbers[51]))