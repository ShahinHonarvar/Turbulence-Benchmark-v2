def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[30:92].lower()
    palindromes = set()
    for i in range(len(substring) - 50):
        for length in range(50, 54):
            if i + length > len(substring) or not substring[i:i + length].isalpha() or substring[i:i + length] != substring[i:i + length][::-1]:
                continue
            palindromes.add(substring[i:i + length])
    return palindromes