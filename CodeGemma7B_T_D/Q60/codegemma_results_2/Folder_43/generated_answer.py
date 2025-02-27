def all_left_right_truncatable_prime(tupl):
    x = tupl[89]
    a = [i for i in range(2, x + 1) if all((j > 1 and i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    b = [i for i in a if str(i) not in '-0' and '0' not in f'{i:.b}' and (str(i) in ''.join(sorted(str(i)[::-1])))]
    return [i for i in b if all_truncatable(i)]

def all_truncatable(i):
    for j in range(len(str(i)) - 1):
        if str(i)[j] == '0':
            return False
        i = int(str(i)[:-j - 1] + str(i)[-j - 1:])
        if i <= 1 or any((i % k == 0 for k in range(2, int(i ** 0.5) + 1))):
            return False
    return True