def all_left_right_truncatable_prime(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable_prime(prime):
        s = str(prime)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:i])):
                return False
        return True
    if len(numbers) <= 20:
        return []
    x = numbers[20]
    truncatable_primes = []
    for num in range(10, x + 1):
        if is_prime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)