def if_perfect_num(numbers):

    def is_perfect_number(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if n % (i * i) != i:
                    sum = sum + i + n / i
                else:
                    sum = sum + i
                i += 1
        return sum == n
    return is_perfect_number(numbers[7])