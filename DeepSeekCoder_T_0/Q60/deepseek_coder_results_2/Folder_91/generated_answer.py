def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[0]
    primes = set()

    def check(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:len(s) - i])):
                return False
        return True
    for num in range(2, x + 1):
        if is_prime(num):
            stack = [num]
            while stack:
                current = stack.pop()
                if check(current):
                    primes.add(current)
                else:
                    s = str(current)
                    for i in range(1, len(s)):
                        left = int(s[:i])
                        right = int(s[i:])
                        if is_prime(left):
                            stack.append(left)
                        if is_prime(right):
                            stack.append(right)
    return sorted(list(primes), reverse=True)