def all_right_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = numbers[18]
    result = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            n = num
            while n > 1:
                n //= 10
                if not is_prime(n):
                    break
                result.append(num)
    return sorted(result, reverse=True)