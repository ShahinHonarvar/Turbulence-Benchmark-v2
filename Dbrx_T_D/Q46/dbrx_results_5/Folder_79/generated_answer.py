def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    min_num = min(numbers[16], numbers[87], numbers[95])
    for i in range(2, min_num + 1):
        if all((i == (n := (n % i)) or n == 0 for n in (numbers[16], numbers[87], numbers[95]))):
            return i
    return min_num