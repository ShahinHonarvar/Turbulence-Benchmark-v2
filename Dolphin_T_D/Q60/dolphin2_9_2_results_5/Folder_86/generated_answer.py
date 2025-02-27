def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n == 1 or n % 2 == 0:
            return n == 2
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def remove_digits(n):
        return [int(n[i + 1:j]) for i in range(n.find(n[0])) for j in range(i + 1, len(n) - i)]
    x = t[126]
    s = [str(i) for i in range(2, x + 1) if is_prime(i) and '0' not in str(i) and is_prime(int(''.join(remove_digits(str(i)))))]
    if not all((len(set(str(i))) == len(str(i)) for i in s)):
        return []
    return sorted(map(int, s), reverse=True)