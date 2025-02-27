def all_right_truncatable_prime(numbers):
    x = numbers[87]

    def is_right_truncatable_prime(n):
        if n <= 1:
            return False
        for i in range(len(str(n))):
            if int(str(n)[:len(str(n)) - i]) % 2 == 0 and int(str(n)[:len(str(n)) - i]) != 2:
                return False
            if not is_prime(int(str(n)[:len(str(n)) - i])):
                return False
        return True

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    result = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)