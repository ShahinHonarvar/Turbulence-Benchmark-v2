def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
    x = numbers[54]
    result = []
    for num in range(x, 0, -1):
        if '0' not in str(num) and is_prime(num):
            truncation = num
            while truncation > 9:
                truncation //= 10
                if not is_prime(truncation):
                    break
            else:
                result.append(num)
    return sorted(result, reverse=True)