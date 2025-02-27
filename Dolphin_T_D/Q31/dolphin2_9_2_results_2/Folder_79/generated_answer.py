def if_perfect_num(numbers):

    def is_perfect(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            elif n % (i * i) == 0:
                sum += i + n // (i * i)
                i += 1
            else:
                sum += i
                i += 1
        if sum == n and n != 1:
            return True
        else:
            return False
    return is_perfect(numbers[63])