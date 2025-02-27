def all_left_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        s = str(num)
        for i in range(len(s)):
            if not is_prime(int(s[i:])):
                return False
        return True
    x = numbers[466]
    result = []
    for num in range(10, x):
        if '0' not in str(num) and is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)