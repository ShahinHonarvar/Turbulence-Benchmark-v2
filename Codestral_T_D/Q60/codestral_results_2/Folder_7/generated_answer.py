def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_left_truncations(n):
        truncations = []
        while n > 0:
            truncations.append(n)
            n = n // 10
        return truncations

    def get_right_truncations(n):
        truncations = []
        while n > 0:
            truncations.append(n)
            n = n % 10 ** (len(str(n)) - 1)
        return truncations
    x = numbers[803]
    result = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_prime(num):
            left_truncations = get_left_truncations(num)
            right_truncations = get_right_truncations(num)
            if all((is_prime(trunc) for trunc in left_truncations)) and all((is_prime(trunc) for trunc in right_truncations)):
                result.append(num)
    return sorted(result)