def palindromes_of_specific_lengths(string):
    string_low = string.lower()[:21]
    lengths = range(5, 81)
    return set(filter(lambda x: any((x[i] == x[~i] for i in range(len(x) // 2))), [string_low[i:j] for i in range(len(string_low) - 9) for j in range(i + lengths[0], min(i + lengths[-1] + 1, len(string_low) + 10)) if len(set(string_low[i:j])) <= 26]))