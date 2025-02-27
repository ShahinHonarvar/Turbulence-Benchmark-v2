def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(32, 80):
        for j in range(i + 34, min(i + 42, 80)):
            substring = s[i:j]
            lower_substring = substring.lower()
            if lower_substring == lower_substring[::-1] and lower_substring.isalpha():
                palindromes.add(substring)
    return palindromes