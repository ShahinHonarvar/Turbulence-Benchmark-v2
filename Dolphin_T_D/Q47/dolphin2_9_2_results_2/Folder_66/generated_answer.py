def palindromes_of_specific_lengths(s):
    s = s[31:79].lower()
    lengths = set()
    for length in range(35, 42):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                lengths.add(sub)
    return lengths