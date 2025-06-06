def if_perfect_num(numbers):

    def is_perfect(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if i * (n / i) == n:
                    sum = sum + i + n / i
                else:
                    sum = sum + i
                i += 1
        return n == sum
    return is_perfect(numbers[321])