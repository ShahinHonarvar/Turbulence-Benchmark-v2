def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n == 2:
            return True
        elif n == 1 or n % 2 == 0:
            return False
        else:
            for i in range(3, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True
    prime_numbers = []
    for number in range(2, x + 1):
        if '0' in str(number):
            continue
        truncated_left = int(str(number)[1:])
        while truncated_left >= 10:
            truncated_left = int(str(truncated_left)[1:])
        while truncated_left >= 10:
            truncated_left = int(str(truncated_left)[1:])
        truncated_right = int(str(number)[:-1])
        while truncated_right >= 10:
            truncated_right = int(str(truncated_right)[:-1])
        while truncated_right >= 10:
            truncated_right = int(str(truncated_right)[:-1])
        if is_prime(truncated_left) and is_prime(truncated_right):
            prime_numbers.append(number)
    return sorted(prime_numbers, reverse=True)