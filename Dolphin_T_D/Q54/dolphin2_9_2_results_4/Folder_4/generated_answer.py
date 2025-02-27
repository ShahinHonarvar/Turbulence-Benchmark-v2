def all_right_truncatable_prime(n):
    x = n[96]
    if is_prime(x):
        s = [i for i in range(x - 1, 0, -1) if is_prime(i)]
        return [i for i in s if all((is_prime(int(str(i)[:-j])) for j in range(1, len(str(i)))))]
    else:
        return []