def if_perfect_num(numbers):

    def is_perfect(n):
        if n < 2:
            return False
        total = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                total += i + n // i if i != n // i else i
        return total == n
    if len(numbers) > 845:
        return is_perfect(numbers[845])
    return False