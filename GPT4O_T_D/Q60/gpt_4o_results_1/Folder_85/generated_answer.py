def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_right_truncatable(n):
        str_n = str(n)
        length = len(str_n)
        for i in range(length):
            left_trunc = int(str_n[i:]) if str_n[i:] else None
            right_trunc = int(str_n[:length - i]) if str_n[:length - i] else None
            if not (left_trunc and right_trunc):
                return False
            if not (is_prime(left_trunc) and is_prime(right_trunc)):
                return False
        return True
    x = numbers[94]
    result = []
    for number in range(10, x + 1):
        if '0' in str(number):
            continue
        if is_left_right_truncatable(number):
            result.append(number)
    return result