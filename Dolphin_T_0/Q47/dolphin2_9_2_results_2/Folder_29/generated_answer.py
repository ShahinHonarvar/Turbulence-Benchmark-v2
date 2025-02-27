def palindromes_of_specific_lengths(s):
    s = s[15:95]
    palindromes = set()
    for length in range(18, 74):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.lower() == sub[::-1].lower():
                if sub.isalpha():
                    palindromes.add(sub)
    return palindromes