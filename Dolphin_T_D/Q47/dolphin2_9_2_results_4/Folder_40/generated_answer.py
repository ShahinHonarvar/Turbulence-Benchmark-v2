def palindromes_of_specific_lengths(s):
    s = s[0:6].lower()
    palindromes = set()
    for i in range(len(s)):
        if 2 <= len(s) - i < 5:
            for j in range(i + 2, len(s) + 1):
                if s[i:j] == s[i:j][::-1] and all((char.isalpha() for char in s[i:j])):
                    palindromes.add(s[i:j])
    return palindromes