def if_perfect_num(numbers):
    if len(numbers) < 14:
        return False

    def is_perfect(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if n == i:
                    sum = sum + i
                else:
                    sum = sum + i + n // i
                i += 1
        return sum == n and n != 1
    return is_perfect(numbers[13])