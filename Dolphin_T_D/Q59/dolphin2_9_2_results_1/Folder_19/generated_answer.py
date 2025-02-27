def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[67]
    result = []
    for i in range(2, x):
        if is_prime(i) and i % 10 != 0:
            temp = i
            while temp:
                if not is_prime(temp):
                    break
                temp //= 10
            else:
                result.append(i)
    return sorted(result, reverse=True)