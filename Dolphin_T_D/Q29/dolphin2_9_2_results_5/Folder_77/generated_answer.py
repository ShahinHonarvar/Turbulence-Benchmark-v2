def gcf_two_nums(arr):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcd(arr[841], arr[804])