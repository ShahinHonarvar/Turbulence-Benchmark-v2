def all_left_right_truncatable_prime(numbers):
    x = numbers[38]

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

    def is_truncatable(n):
        n_str = str(n)
        for i in range(len(n_str)):
            if not is_prime(int(n_str[i:])) or not is_prime(int(n_str[:len(n_str) - i])):
                return False
        return True
    result = []
    for num in range(11, x + 1):
        if '0' in str(num):
            continue
        if is_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)