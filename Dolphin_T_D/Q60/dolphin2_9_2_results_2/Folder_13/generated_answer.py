def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n < 2:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    x = numbers[784]
    result = []
    for num in range(2, x + 1):
        num_str = str(num)
        if '0' not in num_str:
            while len(num_str) > 1:
                if not is_prime(int(num_str[1:-1])):
                    break
                num_str = num_str[1:-1]
            else:
                result.append(num)
    return result