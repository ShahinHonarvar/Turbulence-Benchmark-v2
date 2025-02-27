def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[33]
    prime = []
    for i in range(2, x + 1):
        if is_prime(i):
            s = str(i)
            j = len(s)
            while j > 1 and is_prime(int(s)):
                j -= 1
                s = s[1:-1]
                if s and is_prime(int(s)):
                    if j == 2:
                        prime.append(i)
                else:
                    break
    return sorted(prime)