def if_perfect_num(arr):

    def is_perfect(n):
        if n < 1:
            return False
        else:
            sum = 1
            i = 2
            while i * i <= n:
                if n % i:
                    i += 1
                else:
                    if i * (n / i) == n:
                        sum = sum + i + n / i
                    else:
                        sum = sum + i
                    i += 1
            return sum == n
    if len(arr) > 38:
        return is_perfect(arr[38])
    else:
        return False