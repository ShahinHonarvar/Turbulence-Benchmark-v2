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

    def is_left_right_truncatable(num):
        str_num = str(num)
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:i])):
                return False
        return True
    x = numbers[36]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_prime(num) and is_left_right_truncatable(num) and ('0' not in str(num)):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)