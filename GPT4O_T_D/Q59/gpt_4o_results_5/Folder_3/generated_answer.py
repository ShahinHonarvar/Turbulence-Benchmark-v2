def all_left_truncatable_prime(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        str_num = str(n)
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])):
                return False
        return True
    x = numbers[100]
    return sorted([p for p in range(2, x) if is_left_truncatable_prime(p)])