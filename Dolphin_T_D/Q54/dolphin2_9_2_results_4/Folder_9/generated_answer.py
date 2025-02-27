def all_right_truncatable_prime(tup):

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

    def is_truncatable(n):
        s = str(n)
        while s:
            if not is_prime(int(s)):
                return False
            s = s[0:-1]
        return True
    prime_list = [7, 11, 13, 17, 23, 29, 31, 59, 61, 67, 83, 89, 97, 113, 131]
    num = tup[29]
    right_truncatable_list = [num for num in prime_list if num < num]
    return sorted(right_truncatable_list, reverse=True)