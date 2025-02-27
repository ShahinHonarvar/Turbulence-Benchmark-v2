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

    def is_left_right_truncatable(prime):
        str_prime = str(prime)
        if '0' in str_prime:
            return False
        for i in range(1, len(str_prime)):
            if not is_prime(int(str_prime[i:])) or not is_prime(int(str_prime[:-i])):
                return False
        return True
    x = numbers[767]
    result = []
    for i in range(10, x + 1):
        if is_prime(i) and is_left_right_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)