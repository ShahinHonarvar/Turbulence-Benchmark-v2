def palindromes_of_specific_lengths(s):
    s = s[11:92].lower()
    lengths = range(17, 67)
    palindromes = set()
    for length in lengths:
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if all((ch.isalpha() for ch in substr)):
                if substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes