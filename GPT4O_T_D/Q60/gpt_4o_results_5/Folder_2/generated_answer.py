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

def truncate_both_directions(n):
    s = str(n)
    truncations = set()
    for i in range(len(s)):
        truncations.add(int(s[i:]))
        truncations.add(int(s[:len(s) - i]))
    return truncations

def is_left_right_truncatable_prime(n):
    return all((is_prime(num) for num in truncate_both_directions(n)))

def all_left_right_truncatable_prime(numbers):
    if len(numbers) < 619:
        return []
    x = numbers[618]
    result = []
    for i in range(10, x + 1):
        if '0' not in str(i) and is_left_right_truncatable_prime(i):
            result.append(i)
    return result