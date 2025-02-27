def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate_left(n):
        return int(str(n)[1:])

    def truncate_right(n):
        return int(str(n)[:-1])
    x = numbers[992]
    result = []
    for n in range(2, x + 1):
        if '0' not in str(n) and is_prime(n):
            truncated_left = n
            truncated_right = n
            while truncated_left > 0:
                if not is_prime(truncated_left):
                    break
                truncated_left = truncate_left(truncated_left)
                if truncated_left < 10:
                    while truncated_right > 0:
                        if not is_prime(truncated_right):
                            break
                        truncated_right = truncate_right(truncated_right)
                        if truncated_right < 10 and is_prime(truncated_right):
                            result.append(n)
    return sorted(result)