def if_perfect_num(numbers):

    def is_perfect_number(n):
        if n < 1:
            return False
        else:
            divisors = [1]
            i = 2
            while i * i <= n:
                if n % i == 0:
                    if n // i == i:
                        divisors.append(i)
                    else:
                        divisors.append(i)
                        divisors.append(n // i)
                i += 1
            if sum(divisors) == 2 * n:
                return True
            else:
                return False
    return is_perfect_number(numbers[69])