def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        length = len(str_n)
        for i in range(1, length):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:length - i])):
                return False
        return True
    try:
        x = numbers[92]
    except IndexError:
        return []
    result = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_prime(num) and is_truncatable_prime(num):
            result.append(num)
    return result