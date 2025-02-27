def palindrome_of_length_at_least_n(x):
    X = [c for c in x.lower() if c.isalpha()]
    length = 81
    return set((X[i:i + length] + X[r:r + length][::-1] for i in range(len(X) - length + 1) for r in range(i, i + length)))