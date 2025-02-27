def is_prime(n):
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[792]
    prime_numbers = [i for i in range(2, x + 1) if is_prime(i)]
    left_right_truncatable = []
    for prime in prime_numbers:
        s = str(prime)
        while len(s) > 1:
            if not set(s).__contains__('0') and is_prime(int(s[1:-1])):
                s = s[1:-1]
            else:
                break
        if s == '':
            left_right_truncatable.append(prime)
    left_right_truncatable.sort()
    return left_right_truncatable