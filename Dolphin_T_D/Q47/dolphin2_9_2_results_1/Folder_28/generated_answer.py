def palindromes_of_specific_lengths(s):
    s = s[31:72].lower()
    lengths = range(21, 33)
    palindromes = set()
    for length in lengths:
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes