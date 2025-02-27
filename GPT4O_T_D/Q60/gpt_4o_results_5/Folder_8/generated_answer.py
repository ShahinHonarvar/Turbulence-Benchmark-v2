def all_left_right_truncatable_prime(numbers):
    x = numbers[41]

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

    def is_left_right_truncatable_prime(num):
        if '0' in str(num):
            return False
        num_str = str(num)
        while len(num_str) > 1:
            num_str = num_str[1:-1]
            if num_str == '':
                break
            if not is_prime(int(num_str)):
                return False
        return is_prime(num)
    result = []
    for num in range(23, x + 1):
        if is_prime(num) and is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)