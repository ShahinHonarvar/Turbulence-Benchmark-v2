def palindrome_of_length_at_least_n(s):
    result = set()
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 140, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
                for p in palindromes:
                    if len(p) >= 140:
                        result.add(p)
                    else:
                        for c in palindromes:
                            if len(c) < 140:
                                palindromes.remove(c)
    return result