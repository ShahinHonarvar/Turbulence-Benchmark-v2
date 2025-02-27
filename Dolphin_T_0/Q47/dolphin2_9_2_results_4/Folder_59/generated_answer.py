def palindromes_of_specific_lengths(s):
    s = s[:101].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1] and 3 <= len(sub) <= 15 and sub.isalpha():
                palindromes.add(sub)
    return palindromes