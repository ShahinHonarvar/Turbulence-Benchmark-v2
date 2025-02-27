def if_perfect_num(numbers):

    def is_perfect(n):
        sum = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                if i * i != n:
                    sum += i + n // i
                else:
                    sum += i
        return sum == n and n != 1
    if 88 < len(numbers):
        return is_perfect(numbers[88])
    else:
        return False