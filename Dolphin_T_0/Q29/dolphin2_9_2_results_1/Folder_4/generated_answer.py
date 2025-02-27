def gcf_two_nums(numbers):
    a = numbers[76]
    b = numbers[57]
    gcf = min([a, b])
    while a % gcf != 0 or b % gcf != 0:
        gcf -= 1
    return gcf