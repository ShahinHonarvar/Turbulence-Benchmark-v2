def all_left_truncatable_prime(t):

    def is_prime(n):
        list1 = [2, 3, 5, 7]
        if n % 2 == 0 or n == 1:
            return n == 2
        for i in range(3, 1 + int(n ** 0.5), 2):
            if n % i == 0:
                return False
            if n % (i + 2) == 0:
                return False
        return True
    list2 = []
    for i in range(1, t[2]):
        if '0' in str(i):
            continue
        if is_prime(i) and i != 2:
            if all((is_prime(int(str(i)[n:])) for n in range(1, len(str(i)) + 1))):
                list2.append(i)
    return sorted(list2)