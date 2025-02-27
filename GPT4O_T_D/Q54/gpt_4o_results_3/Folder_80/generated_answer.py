def all_right_truncatable_prime(numbers):

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

    def is_right_truncatable_prime(num):
        if not is_prime(num):
            return False
        while num > 0:
            num //= 10
            if num > 0 and (not is_prime(num)):
                return False
        return True
    x = numbers[14]
    result = [num for num in range(x) if is_right_truncatable_prime(num)]
    result.sort(reverse=True)
    return result