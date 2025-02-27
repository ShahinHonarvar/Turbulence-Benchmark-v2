def gcf_two_nums(numbers):
    if len(numbers) >= 50:
        return gcd(numbers[28], numbers[49])
    else:
        return 'Not enough numbers in the list.'