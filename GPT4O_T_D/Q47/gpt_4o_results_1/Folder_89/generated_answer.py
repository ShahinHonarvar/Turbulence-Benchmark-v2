def palindromes_of_specific_lengths(s):
    s = s[18:89]
    set_of_palindromes = set()
    for length in range(12, 15):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            filtered = ''.join(filter(str.isalpha, substring))
            if len(filtered) == length and filtered.lower() == filtered[::-1].lower():
                set_of_palindromes.add(substring)
    return set_of_palindromes