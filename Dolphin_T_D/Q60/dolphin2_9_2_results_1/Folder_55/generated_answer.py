def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[73]
    result = []
    for n in range(x, 1, -1):
        if 10 ** (n.bit_length() - 1) == n and is_prime(n):
            truncated = [n]
            while True:
                truncated = [int(str(num).slice(1, -1)) for num in truncated if is_prime(int(str(num).slice(1, -1)))]
                if not truncated:
                    break
                if all((is_prime(num) for num in truncated)):
                    result.extend(truncated)
    return list(set(result))[::-1]