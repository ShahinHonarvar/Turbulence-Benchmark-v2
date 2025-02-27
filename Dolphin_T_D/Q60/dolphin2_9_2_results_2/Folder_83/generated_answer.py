def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[24]
    result = []
    for i in range(2, x + 1):
        if '0' in str(i):
            continue
        if is_prime(i):
            left_right_truncatable = True
            for _ in range(len(str(i)) - 2):
                i = int(str(i)[1:-1])
                if i < 2 or not is_prime(i):
                    left_right_truncatable = False
                    break
            if left_right_truncatable:
                result.append(i)
    result.sort()
    return result