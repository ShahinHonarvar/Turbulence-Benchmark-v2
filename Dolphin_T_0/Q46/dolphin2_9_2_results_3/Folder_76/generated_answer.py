def gcf_three_nums(arr):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcd(gcd(arr[876], arr[203]), arr[100])