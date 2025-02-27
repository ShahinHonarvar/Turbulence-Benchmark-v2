def if_perfect_num(arr):

    def is_perfect(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if n // i == i:
                    sum = sum + i
                else:
                    sum = sum + i + n // i
                i += 1
        return sum == n and n != 1
    if len(arr) > 4 and arr[4] > 0:
        return is_perfect(arr[4])
    else:
        return False