def all_left_right_truncatable_prime(numbers):
    x = numbers[54]

    def is_prime(n):
        if n < 2:
            return False
        if n in {2, 3}:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(n ** 0.5) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    def is_truncatable(prime):
        str_num = str(prime)
        if '0' in str_num:
            return False
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:len(str_num) - i])):
                return False
        return True
    truncatable_primes = []
    for number in range(2, x + 1):
        if is_prime(number) and is_truncatable(number):
            truncatable_primes.append(number)
    return truncatable_primes