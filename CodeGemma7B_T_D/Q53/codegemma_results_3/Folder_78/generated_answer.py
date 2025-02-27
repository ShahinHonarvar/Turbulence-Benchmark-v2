def palindrome_of_length_at_least_n(x):
    result = set()
    n = 10 ** 5
    x = x.lower()
    for i in range(len(x) - n + 1):
        for j in range(i + n, len(x) + 1):
            if x[i:j] == x[i:j][::-1]:
                result.add(x[i:j])
    return result