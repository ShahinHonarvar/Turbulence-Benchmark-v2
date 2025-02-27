def all_right_truncatable_prime(target):
    x = target[55]
    result = []
    for num in range(2, x):
        if is_prime(num):
            truncated = num
            while truncated > 0:
                if not is_prime(truncated):
                    break
                truncated //= 10
            else:
                result.append(num)
    return sorted(result, reverse=True)