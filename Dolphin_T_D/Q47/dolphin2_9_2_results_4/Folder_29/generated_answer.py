def palindromes_of_specific_lengths(s):
    substrings = [s[i:j + 1] for i in range(15, 95) for j in range(i, 95)]
    substrings = [substring for substring in substrings if 18 <= len(substring) <= 73]
    substrings = [substring for substring in substrings if substring.isalpha()]
    substrings = [substring.lower() for substring in substrings]
    palindromes = [substring for substring in substrings if substring == substring[::-1]]
    return set(palindromes)