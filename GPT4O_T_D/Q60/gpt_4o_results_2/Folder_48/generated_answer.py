def all_left_right_truncatable_prime(numbers):

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

    def left_right_truncatable(prime):
        str_prime = str(prime)
        length = len(str_prime)
        for i in range(1, length):
            if not is_prime(int(str_prime[i:])) or not is_prime(int(str_prime[:i])):
                return False
        return True
    if len(numbers) <= 835:
        return []
    x = numbers[835]
    result = []
    for i in range(11, x + 1):
        if '0' in str(i):
            continue
        if is_prime(i) and left_right_truncatable(i):
            result.append(i)
    return sorted(result)