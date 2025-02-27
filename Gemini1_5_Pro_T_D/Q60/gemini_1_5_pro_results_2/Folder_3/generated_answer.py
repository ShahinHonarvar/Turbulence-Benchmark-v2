def all_left_right_truncatable_prime(numbers):
    x = numbers[100]

    def is_truncatable_prime(n):
        if n < 10:
            return False
        if '0' in str(n):
            return False
        if not all([int(str(n)[i:]) in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] for i in range(len(str(n)))]):
            return False
        if not all([int(str(n)[:j]) in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] for j in range(1, len(str(n)))]):
            return False
        return True
    result = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            result.append(i)
    return result