def if_perfect_num(numbers):

    def is_perfect_number(n):
        if n < 1:
            return False
        else:
            sum = 1
            i = 2
            while i * i <= n:
                if n % i:
                    i += 1
                elif i * (n // i) == n:
                    sum = sum + i
                    i += 1
                else:
                    sum = sum + i
                    sum = sum + n // i
                    i += 1
            return sum == n and n != 1
    if len(numbers) >= 8:
        return is_perfect_number(numbers[7])
    else:
        return False