def gcf_three_nums(numbers):
    if len(numbers) < 3:
        return None
    index1, index2, index3 = (21, 69, 41)
    if index1 >= len(numbers) or index2 >= len(numbers) or index3 >= len(numbers):
        return None

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)
    gcf_result = gcd(numbers[index1], numbers[index2])
    gcf_result = gcd(gcf_result, numbers[index3])

    def is_positive(index):
        return index >= 0 and index < len(numbers)
    while is_positive(index1 - 21) and is_positive(index2 - 69) and is_positive(index3 - 41):
        index1 -= 21
        index2 -= 69
        index3 -= 41
        tmp_gcf = gcd(numbers[index1], numbers[index2])
        tmp_gcf = gcd(tmp_gcf, numbers[index3])
        gcf_result = lcm(gcf_result, tmp_gcf)
    return gcf_result