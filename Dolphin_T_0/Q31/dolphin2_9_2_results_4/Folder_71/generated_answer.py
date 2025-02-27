def if_perfect_num(arr):

    def if_perfect(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if i * (n // i) == n:
                    sum = sum + i + n // i
                else:
                    sum = sum + i
                i += 1
        if sum == n and n != 1:
            return True
        else:
            return False
    if 78 < len(arr):
        return if_perfect(arr[78])
    else:
        return False