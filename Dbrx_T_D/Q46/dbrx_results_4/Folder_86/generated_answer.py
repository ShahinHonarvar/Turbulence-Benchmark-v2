def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    gcf = gcd(numbers[341], numbers[238])
    gcf = gcd(gcf, numbers[374])
    return gcf