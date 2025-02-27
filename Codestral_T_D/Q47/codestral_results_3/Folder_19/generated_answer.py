def palindromes_of_specific_lengths(s):
    s = s[10:56]
    palindromes = set()
    for i in range(len(s)):
        for j in range(3, 8):
            if i + j <= len(s):
                sub = s[i:i + j]
                if sub.lower() == sub[::-1].lower() and sub.isalpha():
                    palindromes.add(sub)
    return palindromes