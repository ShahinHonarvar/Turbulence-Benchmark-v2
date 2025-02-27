def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[70]
    result = []
    for i in range(2, x):
        if is_prime(i):
            n = i
            while n != 0:
                if not is_prime(n):
                    break
                n //= 10
            else:
                result.append(i)
    return sorted(result, reverse=True)