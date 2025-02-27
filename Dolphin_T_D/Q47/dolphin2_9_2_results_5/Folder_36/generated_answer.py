def palindromes_of_specific_lengths(s):
    s = s[124:284]
    palindromes = set()
    for length in range(115, 135):
        for i in range(0, len(s)):
            if s[i:i + length].lower() == s[i:i + length][::-1].lower():
                for c in s[i:i + length]:
                    if not c.isalpha():
                        break
                else:
                    palindromes.add(s[i:i + length])
    return palindromes