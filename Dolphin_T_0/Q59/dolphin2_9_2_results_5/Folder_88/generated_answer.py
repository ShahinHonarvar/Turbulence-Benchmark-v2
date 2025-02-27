def all_left_truncatable_prime(num):
    x = list(num)[93]
    prime_list = []
    for i in range(2, x):
        if all((i % j != 0 for j in range(2, i))):
            s = str(i)
            if '0' not in s:
                flat = True
                for ch in s:
                    if all((int(ch + s[:j]) != 0 and i % int(ch + s[:j]) != 0 for j in range(1, len(s) - 1))):
                        flat = False
                        break
                if flat:
                    prime_list.append(i)
    return sorted(prime_list)