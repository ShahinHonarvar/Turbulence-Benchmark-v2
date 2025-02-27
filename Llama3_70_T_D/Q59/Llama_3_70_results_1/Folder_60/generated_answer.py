def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable(n):
        s = str(n)
        for i in range(len(s)):
            if not is_prime(int(s[i:])):
                return False
        return True
    x = numbers[87]
    result = []
    for i in range(2, x):
        if '0' not in str(i) and is_prime(i) and left_truncatable(i):
            result.append(i)
    return sorted(result)