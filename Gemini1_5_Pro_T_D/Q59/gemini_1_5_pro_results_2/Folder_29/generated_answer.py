def all_left_truncatable_prime(numbers):
    x = numbers[55]

    def is_left_truncatable_prime(n):
        if n < 10 and n in (2, 3, 5, 7):
            return True
        if '0' in str(n) or any((int(str(n)[i:]) not in (2, 3, 5, 7) for i in range(len(str(n))))):
            return False
        return all((n % int(digit) for digit in str(n))) and all((int(str(n)[:i]) in (2, 3, 5, 7) for i in range(1, len(str(n)))))
    result = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result