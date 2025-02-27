def palindromes_of_specific_lengths(s):
    substrings = s[31:92]
    lengths = range(50, 54)
    palindromes_set = set()
    for length in lengths:
        for i in range(len(substrings) - length + 1):
            substring = substrings[i:i + length]
            if substring[::-1] in palindromes_set:
                palindromes_set.add(substring.lower())
    return palindromes_set