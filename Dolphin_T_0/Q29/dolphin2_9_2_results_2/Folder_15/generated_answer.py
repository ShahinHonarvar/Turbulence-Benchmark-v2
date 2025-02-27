def gcf_two_nums(numbers):
    if len(numbers) < 2:
        return None
    a = numbers[0]
    b = numbers[1]
    while b != 0:
        a, b = (b, a % b)
    return a