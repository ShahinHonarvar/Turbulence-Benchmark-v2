def gcf_three_nums(numbers):
    gcf = numbers[92]
    for i in [69, 95]:
        gcf = gcd(gcf, numbers[i])
    return gcf