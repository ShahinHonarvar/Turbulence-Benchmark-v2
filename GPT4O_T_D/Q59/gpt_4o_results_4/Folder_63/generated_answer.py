def all_left_truncatable_prime(numbers):

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

    def is_left_truncatable(num):
        s = str(num)
        return all((is_prime(int(s[i:])) for i in range(len(s))))
    threshold = numbers[88]
    left_truncatable_primes = []
    for number in range(2, threshold):
        if is_prime(number) and is_left_truncatable(number) and ('0' not in str(number)):
            left_truncatable_primes.append(number)
    return sorted(left_truncatable_primes)