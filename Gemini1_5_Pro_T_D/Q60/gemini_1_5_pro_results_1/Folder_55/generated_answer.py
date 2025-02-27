def all_left_right_truncatable_prime(numbers):
    x = numbers[73]

    def is_truncatable_prime(num):
        if num <= 1 or '0' in str(num):
            return False
        s = str(num)
        for i in range(len(s)):
            if int(s[i:]) not in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] or int(s[:len(s) - i]) not in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
                return False
        return True
    result = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result