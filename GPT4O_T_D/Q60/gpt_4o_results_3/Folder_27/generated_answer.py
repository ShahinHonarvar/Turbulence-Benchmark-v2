def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncatable_primes(n):
        s = str(n)
        for i in range(len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:len(s) - i])):
                return False
        return True
    x = numbers[79]
    result = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_prime(num) and truncatable_primes(num):
            result.append(num)
    return sorted(result, reverse=True)