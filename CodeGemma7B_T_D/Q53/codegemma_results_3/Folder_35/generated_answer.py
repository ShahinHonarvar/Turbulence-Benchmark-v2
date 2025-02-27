def palindrome_of_length_at_least_n(x: str) -> set:
    y = set()

    def get(k, i):
        if i - k + 1 < n or i + k - 1 >= len(x) or x[i - k + 1].lower() != x[i + k - 1].lower():
            return
        y.add(x[i - k + 1:i + k])
        get(k, i - 1)
        get(k + 1, i + 1)
    n = 26
    for k in range(n):
        for i in range(k, len(x)):
            get(k, i)
    return y