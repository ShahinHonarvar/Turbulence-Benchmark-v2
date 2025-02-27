def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable(n):
        s = str(n)
        for i in range(len(s)):
            if not is_prime(int(s[i:])):
                return False
        return True
    x = numbers[22]
    left_truncatables = [i for i in range(2, x) if left_truncatable(i) and '0' not in str(i)]
    return sorted(left_truncatables, reverse=True)