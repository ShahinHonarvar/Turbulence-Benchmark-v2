def if_perfect_num(numbers):

    def is_perfect(n):
        if n == 1:
            return True
        else:
            half = n / 2
            for i in range(1, int(half) + 1):
                if n % i == 0:
                    perfect = is_perfect(n - i)
                    if perfect:
                        return True
            return False
    return is_perfect(numbers[57])