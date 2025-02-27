def all_left_right_truncatable_prime(numbers):
    x = numbers[97]

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

    def is_truncatable(num):
        if '0' in str(num):
            return False
        s = str(num)
        for i in range(len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:i + 1])):
                return False
        return True
    truncatable_primes = []
    for i in range(10, x + 1):
        if is_truncatable(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)