def all_left_truncatable_prime(numbers):
    x = numbers[38]

    def is_left_truncatable_prime(n):
        if n < 10:
            return n in [2, 3, 5, 7]
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            if int(s[i:]) not in [2, 3, 5, 7] and (not (int(s[i:]) > 7 and all((int(s[i:]) % j for j in range(3, int(int(s[i:]) ** 0.5) + 1, 2))))):
                return False
        return all((n % i for i in range(3, int(n ** 0.5) + 1, 2))) if n > 2 else n == 2
    result = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    result.sort(reverse=True)
    return result