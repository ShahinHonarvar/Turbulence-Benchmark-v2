def if_perfect_num(numbers):

    def is_perfect_num(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if n % (i * i) == i:
                    sum = sum + i
                i += 1
        return sum == n
    if len(numbers) > 16 and numbers[16] >= 0:
        if is_perfect_num(numbers[16]):
            return True
    return False