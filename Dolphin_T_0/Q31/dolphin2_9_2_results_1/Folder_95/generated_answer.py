def if_perfect_num(arr):

    def is_perfect(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if i * (n // i) == n:
                    sum += i + n // i
                else:
                    sum += i
                i += 1
        return sum == n and n != 1
    if len(arr) > 87:
        return is_perfect(arr[87])
    else:
        return False