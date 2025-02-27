def all_left_truncatable_prime(numbers):

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

    def is_left_truncatable(num):
        s = str(num)
        for i in range(len(s)):
            if not is_prime(int(s[i:])):
                return False
        return True
    x = numbers[630]
    left_truncatable_primes = [num for num in range(2, x) if '0' not in str(num) and is_left_truncatable(num)]
    return sorted(left_truncatable_primes, reverse=True)