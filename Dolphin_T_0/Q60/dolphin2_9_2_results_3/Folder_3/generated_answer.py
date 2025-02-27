def all_left_right_truncatable_prime(t):
    x = t[100]
    prime = [2, 3]
    for num in range(4, x + 1):
        if all((num % p != 0 for p in prime[:int(num ** 0.5) + 1])):
            prime.append(num)
            break
    return [p for p in prime if str(p).startswith('1') and str(p).endswith('3') and all((int(str(p)[i + 1:j]) in prime for i in range(111) for j in range(1, len(str(p)) - i)))]