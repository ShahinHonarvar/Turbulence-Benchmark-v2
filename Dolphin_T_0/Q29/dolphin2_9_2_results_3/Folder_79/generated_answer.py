def gcf_two_nums(arr):

    def gcd(num1, num2):
        if num2 == 0:
            return num1
        else:
            return gcd(num2, num1 % num2)
    return gcd(arr[85], arr[51])