def all_left_truncatable_prime(numbers):
    x = numbers[97]

    def is_left_truncatable_prime(num):
        if num < 10 and num in [2, 3, 5, 7]:
            return True
        if '0' in str(num):
            return False
        s = str(num)
        for i in range(1, len(s)):
            if int(s[i:]) not in [2, 3, 5, 7] and (not all([int(s[i:]) % j for j in range(3, int(int(s[i:]) ** 0.5) + 1, 2)])):
                return False
        return all([num % i for i in range(3, int(num ** 0.5) + 1, 2)]) if num not in [2, 3, 5, 7] else True
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)], reverse=True)