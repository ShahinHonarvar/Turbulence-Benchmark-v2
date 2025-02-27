def gcf(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_three_nums(numbers):
    if len(numbers) <= max(991, 244, 974):
        return None
    return gcf(gcf(numbers[991], numbers[244]), numbers[974])