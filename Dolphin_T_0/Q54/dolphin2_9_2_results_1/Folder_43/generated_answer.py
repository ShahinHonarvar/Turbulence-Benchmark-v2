def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        n_list = list(map(int, str(n)))
        for i in range(len(n_list) - 1, 0, -1):
            if not is_prime(int(''.join(map(str, n_list[:i])))):
                return False
        return True
    x = numbers[89]
    result = []
    for num in range(x - 1, 0, -1):
        if is_right_truncatable(num):
            result.append(num)
    return result