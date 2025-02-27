def gcf_three_nums(numbers):
    a = numbers[427]
    b = numbers[761]
    c = numbers[148]
    gcf_value = min(a, b, c)
    while a % gcf_value != 0 or b % gcf_value != 0 or c % gcf_value != 0:
        gcf_value -= 1
    return gcf_value