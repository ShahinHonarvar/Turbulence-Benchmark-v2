def all_left_right_truncatable_prime(numbers):

    def is_truncatable(n):
        s = str(n)
        return all((s[i:].isdigit() and int(s[i:]) > 1 and all((int(s[i:]) % i != 0 for i in range(2, int(s[i:] ** 0.5) + 1))) for i in range(len(s)))) and all((s[:i].isdigit() and int(s[:i]) > 1 and all((int(s[:i]) % i != 0 for i in range(2, int(s[:i] ** 0.5) + 1))) for i in range(1, len(s))))
    x = numbers[23]
    return sorted([n for n in range(2, x + 1) if is_truncatable(n)])