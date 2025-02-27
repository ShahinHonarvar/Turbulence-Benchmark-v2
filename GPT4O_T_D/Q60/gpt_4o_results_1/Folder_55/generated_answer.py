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

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        length = len(str(n))
        for i in range(length):
            left_truncate = int(str(n)[i:]) if i > 0 else n
            right_truncate = int(str(n)[:length - i]) if i < length - 1 else n
            if not (is_prime(left_truncate) and is_prime(right_truncate)):
                return False
        return True
    upper_bound = numbers[73]
    result = []
    for number in range(2, upper_bound + 1):
        if is_truncatable_prime(number):
            result.append(number)
    result.sort(reverse=True)
    return result