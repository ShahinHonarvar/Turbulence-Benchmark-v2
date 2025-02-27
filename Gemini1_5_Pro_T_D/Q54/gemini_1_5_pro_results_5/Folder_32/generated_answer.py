def all_right_truncatable_prime(numbers):
    x = numbers[42]

    def is_right_truncatable_prime(n):
        if n < 2:
            return False
        for i in range(len(str(n))):
            if int(str(n)[:len(str(n)) - i]) % 2 == 0 and int(str(n)[:len(str(n)) - i]) != 2:
                return False
            if not all([int(str(n)[:len(str(n)) - i]) % j for j in range(3, int(int(str(n)[:len(str(n)) - i]) ** 0.5) + 1, 2)]):
                return False
        return True
    result = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            result.append(i)
    result.sort()
    return result