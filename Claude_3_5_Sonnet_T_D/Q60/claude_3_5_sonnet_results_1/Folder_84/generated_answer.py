def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        num = str(n)
        for i in range(len(num)):
            left = int(num[i:])
            right = int(num[:len(num) - i])
            if not is_prime(left) or not is_prime(right):
                return False
        return True
    x = numbers[630]
    result = []
    for num in range(x, 10, -1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return result