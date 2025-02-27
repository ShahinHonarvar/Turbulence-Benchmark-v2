def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def all_left_right_truncatable_prime(numbers):
    text_truncatable_numbers = []
    for number in numbers:
        text = str(number)
        while len(text) > 1:
            if is_prime(int(text)):
                text_truncatable_numbers.append(int(text))
                text = text[1:-1]
            else:
                break
    return sorted(list(set(text_truncatable_numbers)))