def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[2:9].lower()
    for i in range(len(s) - 2):
        for j in range(i + 3, min(i + 5, len(s) + 1)):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes