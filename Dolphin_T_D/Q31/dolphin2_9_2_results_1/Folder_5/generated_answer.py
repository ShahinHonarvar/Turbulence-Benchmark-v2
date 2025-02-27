def if_perfect_num(numbers):

    def is_perfect_num(n):
        res = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                if i == n // i:
                    res = res + i
                else:
                    res = res + i + n // i
        return res == n and n != 1
    if len(numbers) < 68:
        return False
    else:
        return is_perfect_num(numbers[67])