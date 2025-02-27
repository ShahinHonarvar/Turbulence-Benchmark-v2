def all_left_truncatable_prime(t):
    prime_numbers = [2, 3, 5, 7]
    for number in range(11, t[792], 2):
        if all((number % i != 0 for i in range(2, int(number ** 0.5) + 1))):
            notation = [digit for digit in str(number) if digit != '0']
            for _ in range(len(notation)):
                if not any((notation[i:] in str(j) for i in range(len(notation)) for j in prime_numbers)):
                    break
                else:
                    prime_numbers.append(int(''.join(notation[:])))
    return sorted(prime_numbers)