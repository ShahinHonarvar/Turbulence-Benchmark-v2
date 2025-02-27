def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    index_818 = numbers[818]
    index_606 = numbers[606]
    index_873 = numbers[873]
    gcf = gcd(gcd(index_818, index_606), index_873)
    return gcf