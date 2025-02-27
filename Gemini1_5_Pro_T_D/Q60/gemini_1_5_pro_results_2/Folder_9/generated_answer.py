def all_left_right_truncatable_prime(numbers):
    x = numbers[29]

    def is_truncatable_prime(n):
        if n < 10 or '0' in str(n):
            return False
        s = str(n)
        for i in range(1, len(s)):
            if not (int(s[i:]) in {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97} and int(s[:len(s) - i]) in {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}):
                return False
        return True
    return sorted([i for i in range(2, x + 1) if is_truncatable_prime(i)], reverse=True)