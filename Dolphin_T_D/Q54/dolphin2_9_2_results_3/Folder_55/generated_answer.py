def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[73]
    result = []
    for i in range(x - 1, 1, -1):
        while i > 1 and (i % 10 != i or i // 10 % 10 == i % 10):
            i -= 1
        if i == 1:
            break
        while i % 10 in (0, 2, 4, 6, 8):
            i -= 1
            while i > 1 and i % 10 == 0:
                i //= 10
        for j in range(int(i ** 0.5), 0, -1):
            if i % j == 0:
                break
        else:
            if i in result or i - i % 10 in result:
                result.append(i)
    return result[::-1]