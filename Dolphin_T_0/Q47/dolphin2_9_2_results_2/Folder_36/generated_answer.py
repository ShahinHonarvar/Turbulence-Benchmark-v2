def palindromes_of_specific_lengths(s):
    s = s[123:284]
    palindromes = set()
    for length in range(115, 135):
        for i in range(0, len(s) - length + 1):
            if s[i:i + length].lower() == s[i:i + length].lower()[::-1] and s[i:i + length].isalpha():
                palindromes.add(s[i:i + length])
    return palindromes