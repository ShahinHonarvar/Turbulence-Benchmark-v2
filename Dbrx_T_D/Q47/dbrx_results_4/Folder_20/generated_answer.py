def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(20, 75):
        for j in range(36, 43):
            if i + j < 75 and s[i:i + j].lower() == s[i:i + j][::-1].lower():
                palindromes.add(s[i:i + j])
    return palindromes