def all_left_right_truncatable_prime(numbers):
    result = []
    for x in numbers:
        if x < 10:
            continue
        digits = str(x)
        if '0' in digits:
            continue
        left_truncatable = True
        right_truncatable = True
        for i in range(len(digits)):
            if not is_prime(int(digits[i:])):
                right_truncatable = False
            if not is_prime(int(digits[:-i])):
                left_truncatable = False
        if left_truncatable and right_truncatable:
            result.append(x)
    return sorted(result)