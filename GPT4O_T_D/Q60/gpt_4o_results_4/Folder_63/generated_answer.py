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

    def is_truncatable_prime(num):
        if '0' in str(num):
            return False
        s = str(num)
        for i in range(len(s)):
            left_truncate = int(s[i:])
            right_truncate = int(s[:len(s) - i])
            if not is_prime(left_truncate) or not is_prime(right_truncate):
                return False
        return True
    x = numbers[88]
    truncatable_primes = []
    for num in range(10, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes