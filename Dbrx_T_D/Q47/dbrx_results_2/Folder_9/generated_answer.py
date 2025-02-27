def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(0, 301):
        for j in range(50, 61):
            if i + j - 1 <= 300 and i - 1 < len(s) and s[i - 1:i + j].isalpha():
                if s[i - 1:i + j].lower() == s[i - 1:i + j][::-1].lower():
                    palindromes.add(s[i - 1:i + j])
    return palindromes