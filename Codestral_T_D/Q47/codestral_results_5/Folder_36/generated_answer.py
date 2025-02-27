def palindromes_of_specific_lengths(s):
    s = s[124:284]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 115, min(i + 135, len(s)) + 1):
            sub = s[i:j]
            if sub.lower() == sub.lower()[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes